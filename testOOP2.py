class PartyAnimal:
    x=0

    def __init__(self,z):
        self.name= z
        print(self.name, "Constructed")

    def party (self):
      self.x =self.x +1
      print('So far:',self.x)
a =PartyAnimal("anjum")
b =PartyAnimal("veer")
a.party()
b.party()

#extend
class FootBallFan (PartyAnimal):
    points =0
    def touch(self):
        self.points=self.points+7
        self.party()
        print(self.name, 'Points:', self.points)

t= FootBallFan("Tanvir")
t.party()
t.touch()

