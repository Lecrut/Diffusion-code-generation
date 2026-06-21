class Animal:

    def __init__(self, name):
        self.name = name

class Vertebrate(Animal):

    def breathe(self):
        return 'Breathing'

class Mammal(Vertebrate):

    def speak(self):
        return 'Moo'

class Bird(Vertebrate):

    def speak(self):
        return 'Chirp'

class Reptile(Vertebrate):

    def speak(self):
        return 'Sss'

class Amphibian(Vertebrate):

    def speak(self):
        return 'Croak'

class Fish(Animal):

    def swim(self):
        return 'Swimming'
if __name__ == '__main__':
    dog = Mammal('Buddy')
    bird = Bird('Tweety')
    fish = Fish('Nemo')
    print(dog.speak())
    print(bird.speak())
    print(fish.swim())