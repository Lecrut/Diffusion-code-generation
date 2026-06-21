def categorize_animals(animals):
    diet_dict = {
        'herbivore': ['Elephant', 'Giraffe', 'Rabbit', 'Panda'],
        'carnivore': ['Lion', 'Tiger', 'Bear', 'Wolf'],
        'omnivore': ['Monkey', 'Fox', 'Squirrel']
    }
    
    categorized_animals = {'herbivore': [], 'carnivore': [], 'omnivore': []}
    
    for animal in animals:
        if animal in diet_dict['herbivore']:
            categorized_animals['herbivore'].append(animal)
        elif animal in diet_dict['carnivore']:
            categorized_animals['carnivore'].append(animal)
        elif animal in diet_dict['omnivore']:
            categorized_animals['omnivore'].append(animal)
    
    return categorized_animals

if __name__ == '__main__':
    sample_animals = ["Lion", "Tiger", "Elephant", "Bear", "Zebra", "Giraffe", "Monkey"]
    categorized_result = categorize_animals(sample_animals)
    print(categorized_result)