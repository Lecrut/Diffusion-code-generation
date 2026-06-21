def categorize_animals(animals):
    endothermic = ['dog', 'cat', 'bird', 'lion', 'cow']
    ectothermic = ['snake', 'fish']
    
    categorized = {'endothermic': [], 'ectothermic': []}
    for animal in animals:
        if animal in endothermic:
            categorized['endothermic'].append(animal)
        elif animal in ectothermic:
            categorized['ectothermic'].append(animal)
    
    return categorized

if __name__ == '__main__':
    sample_animals = ['dog', 'cat', 'bird', 'fish', 'lion', 'cow', 'snake']
    organized_animals = categorize_animals(sample_animals)
    print(organized_animals)