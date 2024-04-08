#Do not forget to enter your selections of number of players required of each category in the beginning.
#Assuming Given Column in Match table of database Players to represent the number of runs bowled by the player.
#Overs Column made in Match table of database Players by dividing entries of column Bowled by 6 since Bowled column represents number of balls given.
#Assuming Maiden Column in Match table of database Players as not needed.

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
MyPlayer=sqlite3.connect('Players.db')
curplayer=MyPlayer.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_4.addWidget(self.lineEdit_7)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.list2)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.list1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuFile.addAction(self.actionNEW_Team)
        self.menuFile.addAction(self.actionOPEN_Team)
        self.menuFile.addAction(self.actionSAVE_Team)
        self.menuFile.addAction(self.actionEVALUATE_Team)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Your Selections"))
        self.label.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.label_2.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.label_3.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.label_4.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.label_6.setText(_translate("MainWindow", "Points Available"))
        self.label_7.setText(_translate("MainWindow", "Points Used"))
        self.radioButton_2.setText(_translate("MainWindow", "BAT"))
        self.radioButton.setText(_translate("MainWindow", "BOW"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_8.setText(_translate("MainWindow", "Team Name"))
        self.menuFile.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def menufunction(self, action):
        txt= (action.text())
        if txt=='NEW Team':
            sql="Select Player from Match"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            for i in range(0,15):
                self.list1.addItem(record[i][0])
            self.lineEdit_5.setText("1000.0")
            self.lineEdit_6.setText("0.0")
            self.radioButton_2.toggled.connect(self.checkstate)
            self.radioButton.toggled.connect(self.checkstate)
            self.radioButton_3.toggled.connect(self.checkstate)
            self.radioButton_4.toggled.connect(self.checkstate)
            self.list1.itemDoubleClicked.connect(self.removelist1)
        if txt =='OPEN Team':
            print("o")
        if txt =='SAVE Team':
            print("s")
        if txt=='EVALUATE Team':
            self.evscore()

    def checkstate(self):
        self.list1.clear()
        if self.radioButton_2.isChecked()==True:
            sql="Select Player from Stats where Ctg=='BAT'"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            for i in range(0,5):
                self.list1.addItem(record[i][0])
        if self.radioButton.isChecked()==True:
            sql="Select Player from Stats where Ctg=='BWL'"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            for i in range(0,4):
                self.list1.addItem(record[i][0])
        if self.radioButton_3.isChecked()==True:
            sql="Select Player from Stats where Ctg=='AR'"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            for i in range(0,4):
                self.list1.addItem(record[i][0])
        if self.radioButton_4.isChecked()==True:
            sql="Select Player from Stats where Ctg=='WK'"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            for i in range(0,2):
                self.list1.addItem(record[i][0])
    
    def removelist1(self, item):
        self.list1.takeItem(self.list1.row(item))
        self.list2.addItem(item.text())
        new_points_used=self.newpoints(item)
        self.lineEdit_6.setText(str(new_points_used))
        self.message()

    def batting(self,runs,balls,four,six):
        points=0
        strikerate=(runs/balls)*100
        if(runs%2==0):
            points=runs/2
        if(runs>=50):
            points=points+5
        if(runs>=100):
            points=points+10
        if(strikerate>=80 and strikerate<=100):
            points=points+2
        elif(strikerate>100):
            points=points+4
        points=points+four
        points=points+2*(six)
        return points

    def bowling(self,runs,overs,wkts):
        points=0
        economyrate=runs/overs
        if(wkts>=1):
            points=10*wkts
        if(wkts==3):
            points=points+5   
        if(wkts>=5):
            points=points+10
        if(economyrate>=3.5 and economyrate<=4.5):
            points=points+4
        elif(economyrate>=2 and economyrate<=3.5):
            points=points+7
        elif(economyrate<2):
            points=points+10
        return points

    def fielding(self,catch,stump,run_out):
        points=10*catch
        points=points+(10*stump)
        points=points+(10*run_out)
        return points

    def newpoints(self,item):
        if self.radioButton_2.isChecked()==True:
            sql="Select Scored,Faced,Fours,Sixes from Match where Player=='"+item.text()+"'"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            x=record[0][0]
            y=record[0][1]
            z=record[0][2]
            w=record[0][3]
            points_used=self.batting(x,y,z,w)
            new_points_available=float(self.lineEdit_5.text())-points_used
            self.lineEdit_5.setText(str(new_points_available))
            points_used=points_used+float(self.lineEdit_6.text())
        if self.radioButton.isChecked()==True:
            sql="Select Given,Overs,Wkts from Match where Player=='"+item.text()+"'"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            x=record[0][0]
            y=record[0][1]
            z=record[0][2]
            points_used=self.bowling(x,y,z)
            new_points_available=float(self.lineEdit_5.text())-points_used
            self.lineEdit_5.setText(str(new_points_available))
            points_used=points_used+float(self.lineEdit_6.text())
        if self.radioButton_4.isChecked()==True:
            sql="Select Catches,Stumping,RO from Match where Player=='"+item.text()+"'"
            curplayer.execute(sql)
            record=curplayer.fetchall()
            x=record[0][0]
            y=record[0][1]
            z=record[0][2]
            points_used=self.fielding(x,y,z)
            new_points_available=float(self.lineEdit_5.text())-points_used
            self.lineEdit_5.setText(str(new_points_available))
            points_used=points_used+float(self.lineEdit_6.text())
        if self.radioButton_3.isChecked()==True:
            if item.text()=='Ashwin':
                sql="Select Scored,Faced,Fours,Sixes,Given,Overs,Wkts,Catches,Stumping,RO from Match where Player=='Ashwin'"
                curplayer.execute(sql)
                record=curplayer.fetchall()
                x=record[0][0]
                y=record[0][1]
                z=record[0][2]
                w=record[0][3]
                p=record[0][4]
                q=record[0][5]
                a=record[0][6]
                b=record[0][7]
                c=record[0][8]
                d=record[0][9]
                points_used=self.batting(x,y,z,w)+self.bowling(p,q,a)+self.fielding(b,c,d)
                new_points_available=float(self.lineEdit_5.text())-points_used
                self.lineEdit_5.setText(str(new_points_available))
                points_used=points_used+float(self.lineEdit_6.text())
            if item.text()=='Bhuvaneshwar':
                sql="Select Scored,Faced,Fours,Sixes,Given,Overs,Wkts,Catches,Stumping,RO from Match where Player=='Bhuvaneshwar'"
                curplayer.execute(sql)
                record=curplayer.fetchall()
                x=record[0][0]
                y=record[0][1]
                z=record[0][2]
                w=record[0][3]
                p=record[0][4]
                q=record[0][5]
                a=record[0][6]
                b=record[0][7]
                c=record[0][8]
                d=record[0][9]
                points_used=self.batting(x,y,z,w)+self.bowling(p,q,a)+self.fielding(b,c,d)
                new_points_available=float(self.lineEdit_5.text())-points_used
                self.lineEdit_5.setText(str(new_points_available))
                points_used=points_used+float(self.lineEdit_6.text())
            if item.text()=='Dhawan':
                sql="Select Scored,Faced,Fours,Sixes,Catches,Stumping,RO from Match where Player=='Dhawan'"
                curplayer.execute(sql)
                record=curplayer.fetchall()
                x=record[0][0]
                y=record[0][1]
                z=record[0][2]
                w=record[0][3]
                a=record[0][4]
                b=record[0][5]
                c=record[0][6]
                points_used=self.batting(x,y,z,w)+self.fielding(a,b,c)
                new_points_available=float(self.lineEdit_5.text())-points_used
                self.lineEdit_5.setText(str(new_points_available))
                points_used=points_used+float(self.lineEdit_6.text())
            if item.text()=='Kartick':
                sql="Select Scored,Faced,Fours,Sixes,Catches,Stumping,RO from Match where Player=='Kartick'"
                curplayer.execute(sql)
                record=curplayer.fetchall()
                x=record[0][0]
                y=record[0][1]
                z=record[0][2]
                w=record[0][3]
                a=record[0][4]
                b=record[0][5]
                c=record[0][6]
                points_used=self.batting(x,y,z,w)+self.fielding(a,b,c)
                new_points_available=float(self.lineEdit_5.text())-points_used
                self.lineEdit_5.setText(str(new_points_available))
                points_used=points_used+float(self.lineEdit_6.text())
        return points_used
            
    def message(self):
        if self.radioButton_2.isChecked()==True and self.list2.count()>int(self.lineEdit.text()):
            self.db1()
        if self.radioButton.isChecked()==True and self.list2.count()>int(self.lineEdit.text())+int(self.lineEdit_2.text()):
            self.db2()
        if self.radioButton_3.isChecked()==True and self.list2.count()>int(self.lineEdit.text())+int(self.lineEdit_2.text())+int(self.lineEdit_3.text()):
            self.db3()
        if self.radioButton_4.isChecked()==True and self.list2.count()>int(self.lineEdit.text())+int(self.lineEdit_2.text())+int(self.lineEdit_3.text())+int(self.lineEdit_4.text()):
            self.db4()

    def db1(self):
        Form1.setObjectName("Form1")
        Form1.resize(247, 79)
        self.formLayout = QtWidgets.QFormLayout(Form1)
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(Form1)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.pushButton1 = QtWidgets.QPushButton(Form1)
        self.pushButton1.setObjectName("pushButton1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton1)
        
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form", "Error"))
        self.label1.setText(_translate("Form", "You can't select more than "+self.lineEdit.text()+" batsmen."))
        self.pushButton1.setText(_translate("Form", "OK"))
        QtCore.QMetaObject.connectSlotsByName(Form1)
        self.pushButton1.clicked.connect(Form1.close)
        
        Form1.show()

    def db2(self):
        Form2.setObjectName("Form2")
        Form2.resize(247, 79)
        self.formLayout = QtWidgets.QFormLayout(Form2)
        self.formLayout.setObjectName("formLayout")
        self.label2 = QtWidgets.QLabel(Form2)
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.pushButton2 = QtWidgets.QPushButton(Form2)
        self.pushButton2.setObjectName("pushButton2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton2)
        
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form", "Error"))
        self.label2.setText(_translate("Form", "You can't select more than "+self.lineEdit_2.text()+" bowler."))
        self.pushButton2.setText(_translate("Form", "OK"))
        QtCore.QMetaObject.connectSlotsByName(Form2)
        self.pushButton2.clicked.connect(Form2.close)
        
        Form2.show()
        
    def db3(self):
        Form3.setObjectName("Form3")
        Form3.resize(247, 79)
        self.formLayout = QtWidgets.QFormLayout(Form3)
        self.formLayout.setObjectName("formLayout")
        self.label3 = QtWidgets.QLabel(Form3)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label3)
        self.pushButton3 = QtWidgets.QPushButton(Form3)
        self.pushButton3.setObjectName("pushButton3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton3)
        
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form", "Error"))
        self.label3.setText(_translate("Form", "You can't select more than "+self.lineEdit_3.text()+" all-rounder."))
        self.pushButton3.setText(_translate("Form", "OK"))
        QtCore.QMetaObject.connectSlotsByName(Form3)
        self.pushButton3.clicked.connect(Form3.close)
        
        Form3.show()

    def db4(self):
        Form4.setObjectName("Form4")
        Form4.resize(247, 79)
        self.formLayout = QtWidgets.QFormLayout(Form4)
        self.formLayout.setObjectName("formLayout")
        self.label4 = QtWidgets.QLabel(Form4)
        self.label4.setObjectName("label4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label4)
        self.pushButton4 = QtWidgets.QPushButton(Form4)
        self.pushButton4.setObjectName("pushButton4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton4)
       
        _translate = QtCore.QCoreApplication.translate
        Form4.setWindowTitle(_translate("Form", "Error"))
        self.label4.setText(_translate("Form", "You can't select more than "+self.lineEdit_4.text()+" wicket-keeper."))
        self.pushButton4.setText(_translate("Form", "OK"))
        self.pushButton4.clicked.connect(Form4.close)
        QtCore.QMetaObject.connectSlotsByName(Form2)

        Form4.show()

    def evscore(self):
        Form.setObjectName("Form")
        Form.resize(503, 420)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 10, 241, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 40, 251, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 100, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 201, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 370, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(250, 120, 231, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(250, 148, 231, 201))
        self.listWidget_2.setObjectName("listWidget_2")

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluate the score of your fantasy team"))
        self.comboBox.setCurrentText(_translate("Form", "Select Team"))
        self.comboBox.setItemText(0, _translate("Form", "Select Team"))
        self.comboBox.setItemText(1, _translate("Form", "Rashika1"))
        self.comboBox.setItemText(2, _translate("Form", "Python1"))
        self.comboBox.setItemText(3, _translate("Form", "Java Team"))
        self.comboBox.setItemText(4, _translate("Form", "C++ Team"))
        self.comboBox_2.setItemText(0, _translate("Form", "Select Match"))
        self.comboBox_2.setItemText(1, _translate("Form", "Match 1"))
        self.comboBox_2.setItemText(2, _translate("Form", "Match 2"))
        self.comboBox_2.setItemText(3, _translate("Form", "Match 3"))
        self.comboBox_2.setItemText(4, _translate("Form", "Match 4"))
        self.comboBox_2.setItemText(5, _translate("Form", "Match 5"))
        self.comboBox_2.setItemText(6, _translate("Form", "Match 6"))
        self.comboBox_2.setItemText(7, _translate("Form", "Match 7"))
        self.comboBox_2.setItemText(8, _translate("Form", "Match 8"))
        self.label_2.setText(_translate("Form", "Players"))
        self.pushButton.setText(_translate("Form", "Calculate Score"))
        self.label_3.setText(_translate("Form", "Points"))
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.addplayer()
        self.pushButton.clicked.connect(self.addpoints)
        
        Form.show()

    def addplayer(self):
        sql1="Select Match.Player from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BAT'"
        curplayer.execute(sql1)
        record1=curplayer.fetchall()
        for i in range(0,5):
            self.listWidget.addItem(record1[i][0])
        sql2="Select Match.Player from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BWL'"
        curplayer.execute(sql2)
        record2=curplayer.fetchall()
        for i in range(0,4):
            self.listWidget.addItem(record2[i][0])
        sql3="Select Match.Player from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql3)
        record3=curplayer.fetchall()
        for i in range(0,4):
            self.listWidget.addItem(record3[i][0])
        sql4="Select Match.Player from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='WK'"
        curplayer.execute(sql4)
        record4=curplayer.fetchall()
        for i in range(0,2):
            self.listWidget.addItem(record4[i][0])

    def batpoints(self):
        sql1="Select Scored from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BAT'"
        curplayer.execute(sql1)
        record1=curplayer.fetchall()
        sql2="Select Faced from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BAT'"
        curplayer.execute(sql2)
        record2=curplayer.fetchall()
        sql3="Select Fours from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BAT'"
        curplayer.execute(sql3)
        record3=curplayer.fetchall()
        sql4="Select Sixes from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BAT'"
        curplayer.execute(sql4)
        record4=curplayer.fetchall()
        points_available=0
        for i in range(0,5):
            x=record1[i][0]
            y=record2[i][0]
            z=record3[i][0]
            w=record4[i][0]
            score=self.batting(x,y,z,w)
            self.listWidget_2.addItem(str(score))
            points_available=points_available+score
        return points_available

    def bowlpoints(self):
        sql1="Select Given from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BWL'"
        curplayer.execute(sql1)
        record1=curplayer.fetchall()
        sql2="Select Overs from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BWL'"
        curplayer.execute(sql2)
        record2=curplayer.fetchall()
        sql3="Select Wkts from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='BWL'"
        curplayer.execute(sql3)
        record3=curplayer.fetchall()
        points_available=0
        for i in range(0,4):
            x=record1[i][0]
            y=record2[i][0]
            z=record3[i][0]
            score=self.bowling(x,y,z)
            self.listWidget_2.addItem(str(score))
            points_available=points_available+score
        return points_available

    def arpoints(self):
        sql1="Select Scored from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql1)
        record1=curplayer.fetchall()
        sql2="Select Faced from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql2)
        record2=curplayer.fetchall()
        sql3="Select Fours from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql3)
        record3=curplayer.fetchall()
        sql4="Select Sixes from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql4)
        record4=curplayer.fetchall()
        sql5="Select Given from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql5)
        record5=curplayer.fetchall()
        sql6="Select Overs from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR' and Match.Overs!=0"
        curplayer.execute(sql6)
        record6=curplayer.fetchall()
        sql6="Select Wkts from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql6)
        record7=curplayer.fetchall()
        sql8="Select Catches from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql8)
        record8=curplayer.fetchall()
        sql9="Select Stumping from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql9)
        record9=curplayer.fetchall()
        sql10="Select RO from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='AR'"
        curplayer.execute(sql10)
        record10=curplayer.fetchall()
        x=record1[0][0]
        y=record2[0][0]
        z=record3[0][0]
        w=record4[0][0]
        a=record8[0][0]
        b=record9[0][0]
        c=record10[0][0]
        points_available0=self.batting(x,y,z,w)+self.fielding(a,b,c)
        self.listWidget_2.addItem(str(points_available0))
        points_available1=0
        j=0
        for i in (1,2):
            x=record1[i][0]
            y=record2[i][0]
            z=record3[i][0]
            w=record4[i][0]
            p=record5[i][0]
            q=record6[j][0]
            a=record7[i][0]
            b=record8[i][0]
            c=record9[i][0]
            d=record10[i][0]
            j=j+1
            score=self.batting(x,y,z,w)+self.bowling(p,q,a)+self.fielding(b,c,d)
            self.listWidget_2.addItem(str(score))
            points_available1=points_available1+score
        x=record1[3][0]
        y=record2[3][0]
        z=record3[3][0]
        w=record4[3][0]
        a=record8[3][0]
        b=record9[3][0]
        c=record10[3][0]
        points_available2=self.batting(x,y,z,w)+self.fielding(a,b,c)
        self.listWidget_2.addItem(str(points_available2))
        points_available=points_available0+points_available1+ points_available2
        return points_available

    def fieldpoints(self):
        sql1="Select Catches from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='WK'"
        curplayer.execute(sql1)
        record1=curplayer.fetchall()
        sql2="Select Stumping from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='WK'"
        curplayer.execute(sql2)
        record2=curplayer.fetchall()
        sql3="Select RO from Match,Stats where Match.Player==Stats.Player and Stats.Ctg=='WK'"
        curplayer.execute(sql3)
        record3=curplayer.fetchall()
        points_available=0
        for i in range(0,2):
            x=record1[i][0]
            y=record2[i][0]
            z=record3[i][0]
            score=self.fielding(x,y,z)
            self.listWidget_2.addItem(str(score))
            points_available=points_available+score
        return points_available

    def addpoints(self):
        self.lineEdit.setText("0.0")
        x=self.batpoints()
        y=self.bowlpoints()
        z=self.arpoints()
        w=self.fieldpoints()
        points=x+y+z+w
        self.lineEdit.setText(str(points))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Form1 = QtWidgets.QWidget()
    Form2 = QtWidgets.QWidget()
    Form3 = QtWidgets.QWidget()
    Form4 = QtWidgets.QWidget()
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
