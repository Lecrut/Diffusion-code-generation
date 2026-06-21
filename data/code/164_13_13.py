def sort_animals_by_type(animals):
    return sorted(animals, key=lambda x: x['type'])

if __name__ == '__main__':
    animals = [
        {'name': 'Elephant', 'type': 'Mammal'},
        {'name': 'Dog', 'type': 'Mammal'},
        {'name': 'Cat', 'type': 'Mammal'},
        {'name': 'Fish', 'type': 'Aquatic'},
        {'name': 'Turtle', 'type': 'Reptile'}
    ]
    sorted_animals = sort_animals_by_type(animals)
    print(sorted_animals)