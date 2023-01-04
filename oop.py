class animal:
    def __init__(self, height,heavy,sex,move): 
        self.height = height
        self.heavy = heavy
        self.move = move 
        self.sex = sex
    
Lion = animal("3ft","700kg","female"," are running")
Lion.type = "Lion"
Bird = animal("25cm","10kg","male"," are flying")
Bird.type = "Bird"
print(Bird.sex + " " +Bird.type + Bird.move) 

class animal:
    name = "Bird"
    def color(self):
        print ("{} are Red".format(self.name))
pinkbird = animal()
pinkbird.name = "pinkbird"
pinkbird.color()
Carolasparotia = animal()
Carolasparotia.name = "Carolasparotia"
Carolasparotia.color()
