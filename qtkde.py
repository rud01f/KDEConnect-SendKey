import sys
import dbus
from PyQt4 import QtGui, QtCore, QtCore

# device id obtained from shell command: kdeconnect-cli --list-devices
DEV_ID = "e8186bba7b4cc868"

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('KDE Connect Input')
        self.show()

    def keyPressEvent(self, e):
        key = e.key()
        shift = QtCore.Qt.ShiftModifier and e.modifiers()
        ctrl = QtCore.Qt.ControlModifier and e.modifiers()
        alt = QtCore.Qt.ControlModifier and e.modifiers()
        
        a0 = kkiface.translateQtKey(key)
        kkiface.sendKeyPress(e.text(), a0, shift, ctrl, alt, signature="sibbb")
        
def main():
    global kkiface
    
    sesbus = dbus.SessionBus()
    kdekbdobj = sesbus.get_object('org.kde.kdeconnect', "/modules/kdeconnect/devices/%s/remotekeyboard" % DEV_ID)
    kkiface = dbus.Interface(kdekbdobj, dbus_interface='org.kde.kdeconnect.device.remotekeyboard')
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
