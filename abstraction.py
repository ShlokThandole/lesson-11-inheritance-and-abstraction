from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass

class monkey(animal):
    def move(self):
        print("i can eat and TREES")

class doratheexplorer(animal):
    def move(self):
        print("i am blind")

class humans(animal):
    def move(self):
        print("i can walk and run")

class sloth(animal):
    def move(self):
        print("i an fast")

M = monkey()
M.move()

D = doratheexplorer()
D.move()

H = humans()
H.move()

S = sloth()
S.move()