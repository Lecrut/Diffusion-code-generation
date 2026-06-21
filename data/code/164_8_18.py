def categorize_animals(animals):
    endothermic = ['dog', 'cat', 'bird', 'lion', 'cow']
    ectothermic = ['snake', 'fish']
    
    result = {'endothermic': [], 'ectothermic': []}
    
    for animal in animals:
        if animal in endothermic:
            result['endothermic'].append(animal)
        elif animal in ectothermic:
            result['ectothermic'].append(animal)
    
    return result

if __name__ == '__main__':
    sample_animals = ["dog", "cat", "bird", "fish", "lion", "cow", "snake"]
    categorized_animals = categorize_animals(sample_animals)
    print(categorized_animals)