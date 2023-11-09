import random


class Player:
    def __init__(self, name, color, accessories):
      self.name = name
      self.color = color
      self.accessories = accessories

class Tripulante(Player):
  def __init__(self, name, color, accessories):
    super().__init__(name, color, accessories)

class Impostor(Player):
  def __init__(self, name, color, accessories):
    super().__init__(name, color, accessories)

def create_player():
  players = []

  for i in range(0,5):
        name = input(f"Nome do Tripulante: ")
        color = input(f"Cor do Tripulante: ")
        accessories = input(f"acessório do Tripulante?")
        players.append(Tripulante(name, color, accessories))

  for i in range(0,5):
        name = input(f"Nome do Impostor: ")
        color = input(f"Cor do Impostor: ")
        accessories = input(f"acessório do Tripulante?")
        players.append(Impostor(name, color, accessories))



  ricardo = Player(name, color, "chapéu")
  print(ricardo.name) 