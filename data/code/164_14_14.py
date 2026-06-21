class Animal:
    def __init__(self, name, type):
        if not isinstance(name, str) or not isinstance(type, str):
            raise ValueError("Name and type must be strings")
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
    mammals = filter_mammals(sample_animals)
    for mammal in mammals:
        print(mammal.name)