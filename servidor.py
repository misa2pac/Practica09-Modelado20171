import sys
from PyQt4 import QtCore, QtGui, uic

w = uic.loadUiType("servidor.ui")[0]

class VentanaServidor(QtGui.QWidget, w):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.spinBox_columnas.valueChanged.connect(self.CambiarColumnas)
		self.spinBox_filas.valueChanged.connect(self.CambiarFilas)

	def CambiarColumnas(self):
		self.tableWidget.setColumnCount(self.spinBox_columnas.value())
	
	def CambiarFilas(self):
		self.tableWidget.setRowCount(self.spinBox_filas.value())

app = QtGui.QApplication(sys.argv)
MiVentana = VentanaServidor(None)
MiVentana.show()
app.exec_()