def sort_animals_by_type(animal_list):
    if not all(isinstance(animal, str) for animal in animal_list):
        raise ValueError("All items in the list must be strings.")
    
    animal_types = {animal.lower(): [] for animal in set(animal_list)}
    
    for animal in animal_list:
        animal_types[animal.lower()].append(animal)
    
    sorted_animals = [sorted(v) for v in animal_types.values()]
    
    return sorted_animals

if __name__ == '__main__':
    sample_animals = [
        "Dog",
        "cat",
        "Bird",
        123,
        "fish",
        "Dog"
    ]
    
    try:
        result = sort_animals_by_type(sample_animals)
        print(result)
    except ValueError as e:
        print(e)