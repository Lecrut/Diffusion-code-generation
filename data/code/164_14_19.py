class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

def filter_mammals(animals):
    if not all(isinstance(animal, Animal) for animal in animals):
        raise ValueError("All elements in the list must be instances of Animal.")
    return [animal for animal in animals if animal.type == 'Mammal']

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