import platform
from datetime import datetime
import os

def desligarMaquina():
    while True:
        data = datetime.now()
        horaMinutoAtual = str(data.hour) + ":" + str(data.minute)
        
        if horaDesejada == horaMinutoAtual:
            if platform.system() == "Linux":
                print("Desligando...")
                os.system("shutdown -h now")
            elif platform.system() == "Windows":
                print("Desligando...")
                os.system("shutdown -s -t 0")
#==============================================================================
horaDesejada = input("Hora em que a maquina sera desligada (Exemplo: 14:15): ")
print("Maquina programada para encerramento as: " + horaDesejada)

desligarMaquina()
