def categorize_animals(animals):
    endothermic = ['dog', 'cat', 'bird', 'lion', 'cow']
    ectothermic = ['snake', 'fish']

    categorized_animals = {'endothermic': [], 'ectothermic': []}

    for animal in animals:
        if animal in endothermic:
            categorized_animals['endothermic'].append(animal)
        elif animal in ectothermic:
            categorized_animals['ectothermic'].append(animal)

    return categorized_animals

if __name__ == '__main__':
    sample_animals = ['dog', 'cat', 'bird', 'fish', 'lion', 'cow', 'snake']
    organized_data = categorize_animals(sample_animals)
    print(organized_data)