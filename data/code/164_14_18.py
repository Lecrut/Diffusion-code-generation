class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

def filter_mammals(animals):
    return [animal for animal in animals if animal.type == 'Mammal']

if __name__ == '__main__':
    sample_animals = [
        Animal('Lion', 'Mammal'),
        Animal('Eagle', 'Bird'),
        Animal('Dog', 'Mammal'),
        Animal('Fish', 'Fish')
    ]
    filtered_mammals = filter_mammals(sample_animals)
    print([mammal.name for mammal in filtered_mammals])