def categorize_animals(animals):
    endothermic = []
    ectothermic = []

    for animal in animals:
        if animal == 'Dog' or animal == 'Cat' or animal == 'Human':
            endothermic.append(animal)
        else:
            ectothermic.append(animal)

    return {'endothermic': endothermic, 'ectothermic': ectothermic}

if __name__ == '__main__':
    animals = ['Dog', 'Snake', 'Cat', 'Turtle', 'Human']
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)