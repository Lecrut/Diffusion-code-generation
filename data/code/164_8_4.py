def categorize_animals(animals):
    endothermic = []
    ectothermic = []

    for animal in animals:
        if animal == 'dog' or animal == 'cat' or animal == 'bird':
            endothermic.append(animal)
        elif animal == 'snake' or animal == 'frog' or animal == 'lizard':
            ectothermic.append(animal)

    return {'endothermic': endothermic, 'ectothermic': ectothermic}

if __name__ == '__main__':
    animals = ['dog', 'cat', 'bird', 'snake', 'frog', 'lizard']
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)