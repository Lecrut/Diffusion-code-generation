def categorize_animals(animals):
    endothermic = []
    ectothermic = []

    for animal in animals:
        if animal == 'dog' or animal == 'cat':
            endothermic.append(animal)
        elif animal == 'snake' or animal == 'frog':
            ectothermic.append(animal)

    return {'endothermic': endothermic, 'ectothermic': ectothermic}

if __name__ == '__main__':
    animals = ['dog', 'cat', 'snake', 'frog']
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)