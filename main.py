from PyQt5.QtWidgets import *
from PyQt5 import uic
import webbrowser
import pyttsx3



class MyGUI(QMainWindow):

	def __init__(self):
		super(MyGUI, self).__init__()
		uic.loadUi("mygui_2.ui", self)
		self.show()

		self.pushButton.clicked.connect(self.login)
		self.pushButton_2.clicked.connect(lambda: self.sayit(self.textEdit.toPlainText()))
		self.actionClose.triggered.connect(exit)
		self.openGmail.clicked.connect(self.open_gmail)
		self.openGithub.clicked.connect(self.open_github)


		# if self.actionClose.triggered.connect(exit):
		# 	print("Closed App!")




	def login(self):
		if self.lineEdit.text() == "kadalisravanthi007@gmail.com" and self.lineEdit_2.text() == "Akki7&Buddi":
			self.textEdit.setEnabled(True)
			self.pushButton_2.setEnabled(True)
		else:
			message = QMessageBox()
			message.setText("Invalid Login!")
			engine = pyttsx3.init()
			def speak(audio):
				engine.say(audio)
				print(f"Mark: {audio}")
				engine.runAndWait()
			speak("Invalid Login!")
			message.exec_()

	def sayit(self, msg):
		message = QMessageBox()
		message.setText(msg)
		message.exec_()



	def open_gmail(self):
		engine = pyttsx3.init()
		def speak(audio):
			engine.say(audio)
			print(f"Mark: {audio}")
			engine.runAndWait()
		speak("Opening Gmail...")
		webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox")

	def open_github(self):
		engine = pyttsx3.init()
		def speak(audio):
			engine.say(audio)
			print(f"Mark: {audio}")
			engine.runAndWait()
		speak("Opening GitHub...")
		webbrowser.open("https://github.com/")




def main():
	app = QApplication([])
	window = MyGUI()
	app.exec_()

if __name__ == "__main__":
	main()				