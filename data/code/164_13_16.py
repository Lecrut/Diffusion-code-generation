def sort_animals_by_type(animal_list):
    if not all(isinstance(item, str) for item in animal_list):
        raise ValueError("All items in the list must be strings.")
    
    unique_animals = set()
    sorted_animals = []
    
    for animal in animal_list:
        unique_animals.add(animal.lower())
        sorted_animals.append((animal, animal.lower()))
    
    sorted_animals.sort(key=lambda x: x[1])
    
    return [animal for animal, _ in sorted_animals]

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
        sorted_animals = sort_animals_by_type(sample_animals)
        print(sorted_animals)
    except ValueError as e:
        print(e)