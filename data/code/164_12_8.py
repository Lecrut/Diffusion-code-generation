class Animal:
    def __init__(self, name):
        self.name = name

class Vertebrate(Animal):
    def __init__(self, name):
        super().__init__(name)

class Mammal(Vertebrate):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Moo"

class Bird(Vertebrate):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Chirp"

class Reptile(Vertebrate):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Sss"

class Amphibian(Vertebrate):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Croak"

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
    def swim(self):
        return "Swimming"

if __name__ == '__main__':
    mammal = Mammal("Dog")
    bird = Bird("Eagle")
    reptile = Reptile("Snake")
    amphibian = Amphibian("Frog")
    fish = Fish("Tuna")

    print(mammal.speak())
    print(bird.speak())
    print(reptile.speak())
    print(amphibian.speak())
    print(fish.swim())