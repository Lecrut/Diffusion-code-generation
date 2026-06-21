class Animal:
    def __init__(self, name):
        self.name = name

class Vertebrate(Animal):
    def breathe(self):
        return "Breathing"

class Mammal(Vertebrate):
    def give_birth(self):
        return "Giving birth to live young"

class Bird(Vertebrate):
    def lay_eggs(self):
        return "Laying eggs"

class Reptile(Vertebrate):
    def shed_skin(self):
        return "Shedding skin"

class Amphibian(Vertebrate):
    def breathe_air_and_water(self):
        return "Breathing air and water"

class Fish(Animal):
    def swim(self):
        return "Swimming"

if __name__ == '__main__':
    mammal = Mammal("Dog")
    bird = Bird("Eagle")
    reptile = Reptile("Snake")
    amphibian = Amphibian("Frog")
    fish = Fish("Salmon")

    print(mammal.breathe())
    print(bird.lay_eggs())
    print(reptile.shed_skin())
    print(amphibian.breathe_air_and_water())
    print(fish.swim())