class Animal:
    def __init__(self, name):
        self.name = name

class Vertebrate(Animal):
    def __init__(self, name):
        super().__init__(name)

class Mammal(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

class Bird(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

class Reptile(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

class Amphibian(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

if __name__ == '__main__':
    mammal = Mammal("Dog")
    bird = Bird("Eagle")
    reptile = Reptile("Snake")
    amphibian = Amphibian("Frog")
    fish = Fish("Salmon")

    print(mammal.name)
    print(bird.name)
    print(reptile.name)
    print(amphibian.name)
    print(fish.name)