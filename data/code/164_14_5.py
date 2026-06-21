class Animal:
    TYPE_MAMMAL = 'Mammal'

    def __init__(self, name, type):
        self.name = name
        self.type = type

    @staticmethod
    def is_mammal(animal):
        return animal.type == Animal.TYPE_MAMMAL

def filter_mammals(animals):
    return [animal for animal in animals if Animal.is_mammal(animal)]

if __name__ == '__main__':
    sample_animals = [
        Animal('Lion', 'Mammal'),
        Animal('Eagle', 'Bird'),
        Animal('Dog', 'Mammal'),
        Animal('Fish', 'Fish')
    ]
    mammals = filter_mammals(sample_animals)
    for mammal in mammals:
        print(mammal.name)