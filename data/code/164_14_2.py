ANIMAL_TYPES = {
    'Mammal': 1,
    'Bird': 2,
    'Fish': 3
}

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type_id = ANIMAL_TYPES[type]

def filter_mammals(animals):
    return [animal for animal in animals if animal.type_id == ANIMAL_TYPES['Mammal']]

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