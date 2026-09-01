from PySide import QtWidgets
def SectionModulusIn(self:Part.Face,column_1_subscript = "",column_2_subscript = None):
	from pandas import DataFrame #to_clipboard 
	'''
	displays height (h), y, I, and Section Mod (S) in inches^3 as a string and copies it to clipboard
	'''
	if column_1_subscript == None:
		column_1_subscript = ""
	else:
		column_1_subscript = " - " + column_1_subscript
	if column_2_subscript == None:
		column_2_subscript = ""
	else:
		column_2_subscript = "_" + column_2_subscript
	df = DataFrame([['Height','h',(self.BoundBox.YMax-self.BoundBox.YMin)/25.4,'in'],
					['Neutral Axis','n',self.CenterOfMass[1]/25.4,'in'],
					['y','y','=MAX(n'+column_2_subscript+',h'+column_2_subscript+'-n'+column_2_subscript+')','in'],
					['Moment of Inertia','h',self.MatrixOfInertia.A11/25.4**4,'in^4'],
					['Area','a',self.Area/25.4**2,'in^2']])
	df[0]+=column_1_subscript
	df[1]+=column_2_subscript

	df.to_clipboard(index=False,header=None)
	App.Console.PrintMessage(df)
	return df

if len(FreeCADGui.Selection.getSelection())==1:
	qd=QtWidgets.QInputDialog()
	s1=QtWidgets.QInputDialog.getText(qd,'Section Modulus Table (in)','Enter Variable Name')
	s2=QtWidgets.QInputDialog.getText(qd,'Section Modulus Table (in)','Enter Subscript')
	
	sub1=s1[0]
	sub2=s2[0]
	
	SectionModulusIn(FreeCADGui.Selection.getSelection()[0].Shape,sub1,sub2)
else:
	App.Console.PrintError('\nExactly 1 Face must be selected')
