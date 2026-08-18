import os

class Dispositivo:

    rede = [
        
    ]

    def __init__(self, dispositivo, categoria):
        self.dispositivo = dispositivo
        self.categoria = categoria
        self.ativo = False
        Dispositivo.rede.append(self)


    def listar_dispositivos():
        for dispostivo in Dispositivo.rede:
            print(f"\nDispositivo: {dispostivo.dispositivo}")
            print(f"Categoria: {dispostivo.categoria}")
            print(f"Ativo: {dispostivo.ativo}")
            print(f"---" * 30)


Dispositivo('Smart Sensor', 'Automação')

Dispositivo.listar_dispositivos()