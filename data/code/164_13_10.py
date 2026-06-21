def sort_animals_by_type(animals):
    return sorted(animals, key=lambda x: x['type'])

if __name__ == '__main__':
    animals = [
        {'name': 'Lion', 'type': 'Predator'},
        {'name': 'Elephant', 'type': 'Herbivore'},
        {'name': 'Turtle', 'type': 'Reptile'},
        {'name': 'Giraffe', 'type': 'Herbivore'}
    ]
    sorted_animals = sort_animals_by_type(animals)
    print(sorted_animals)