import PySimpleGUIQt as s
form=s.FlexForm('My GUI')
layout = [[s.Text('Enter your Name' , size=(15,1)),s.InputText()],
          [s.Text('Enter your Country Name', size=(15,1)),s.InputText()],
          [s.Text('Enter your Phone', size=(15,1)),s.InputText()],
          [s.Text('Enter your City', size=(15,1)),s.InputText()],
          [s.Ok(),s.Cancel()]]
button,values = form.Layout(layout).Read()
print(values[0])
print(f"name = {values[0]}, country = {values[1]}, phone = {values[2]}, city = {values[3]}")