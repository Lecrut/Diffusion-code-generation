def sort_animals_by_type(animals):
    animal_types = {
        'mammals': [],
        'birds': [],
        'reptiles': []
    }
    
    for animal in animals:
        if 'mammal' in animal.lower():
            animal_types['mammals'].append(animal)
        elif 'bird' in animal.lower():
            animal_types['birds'].append(animal)
        elif 'reptile' in animal.lower():
            animal_types['reptiles'].append(animal)
    
    for animal_type in animal_types:
        animal_types[animal_type].sort()
    
    sorted_animals = []
    for animal_type, animals in animal_types.items():
        sorted_animals.extend(animals)
    
    return sorted_animals

if __name__ == '__main__':
    sample_animals = [
        'lion', 'tiger', 'eagle', 'penguin', 'snake', 'crocodile'
    ]
    print(sort_animals_by_type(sample_animals))