def sort_animals_by_type(animals):
    return sorted(animals, key=lambda x: x['type'])

if __name__ == '__main__':
    animals = [
        {'name': 'Lion', 'type': 'Mammal'},
        {'name': 'Eagle', 'type': 'Bird'},
        {'name': 'Turtle', 'type': 'Reptile'},
        {'name': 'Dog', 'type': 'Mammal'}
    ]
    sorted_animals = sort_animals_by_type(animals)
    print(sorted_animals)