def sort_animals_by_type(animals):
    return sorted(animals, key=lambda x: x['type'])

if __name__ == '__main__':
    animals = [
        {'name': 'Lion', 'type': 'Carnivore'},
        {'name': 'Elephant', 'type': 'Herbivore'},
        {'name': 'Turtle', 'type': 'Omnivore'},
        {'name': 'Penguin', 'type': 'Bird'}
    ]
    sorted_animals = sort_animals_by_type(animals)
    print(sorted_animals)