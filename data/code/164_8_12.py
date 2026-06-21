def categorize_animals(animals):
    endothermic = []
    ectothermic = []

    for animal in animals:
        if animal.lower() == 'dog' or animal.lower() == 'cat':
            endothermic.append(animal)
        elif animal.lower() == 'snake' or animal.lower() == 'lizard':
            ectothermic.append(animal)

    return {'endothermic': endothermic, 'ectothermic': ectothermic}

if __name__ == '__main__':
    animals = ['Dog', 'Cat', 'Snake', 'Lizard']
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)