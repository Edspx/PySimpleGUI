import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window


'''layout = [
    [sg.Text('Mailing')], 
    [sg.Input(), sg.FileBrowse()], 
    [sg.OK(), sg.Cancel()]
]

window = sg.Window('Padronizar Mailing', layout)

while True:
    event, values = window.read()
    print(values[0])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break


window.close()'''


#Medidor de Progresso
'''for i in range(1,10000):
    sg.one_line_progress_meter('My Meter', i+1, 10000, 'key','Optional message')'''



#Depuração
'''for i in range(10000):
    sg.Print(i)
'''


layout = [[sg.Text('Enter a filename:')],
          [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse()],
          [sg.B('Save'), sg.B('Exit Without Saving', key='Exit')]]

window = sg.Window('Filename Example', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Save':
        sg.user_settings_set_entry('-filename-', values['-IN-'])

window.close()