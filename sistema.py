import platform
from PyQt5 import uic, QtWidgets
 
my_system = platform.uname()

def dados():
    sistema = tela.lb_1.setText(f'{my_system.system}')
    nome = tela.lb_2.setText(f'{my_system.node}')
    lacamento = tela.lb_3.setText(f'{my_system.release}')
    versao = tela.lb_4.setText(f'{my_system.version}')
    machine = tela.lb_5.setText(f'{my_system.machine}')
    processador = tela.lb_6.setText(f'{my_system.processor}')


app = QtWidgets.QApplication([])
tela = uic.loadUi("sistema.ui")
tela.bt_executar.clicked.connect(dados)

tela.show()
app.exec()