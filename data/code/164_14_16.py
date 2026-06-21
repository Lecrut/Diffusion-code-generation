class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

def filter_mammals(animals):
    return [animal for animal in animals if animal.type == 'Mammal']

if __name__ == '__main__':
    sample_animals = [
        Animal('Lion', 'Mammal'),
        Animal('Penguin', 'Bird'),
        Animal('Elephant', 'Mammal'),
        Animal('Owl', 'Bird')
    ]
    mammals = filter_mammals(sample_animals)
    for mammal in mammals:
        print(mammal.name)