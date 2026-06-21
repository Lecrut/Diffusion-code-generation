def categorize_animals(animals):
    endothermic = []
    ectothermic = []

    for animal in animals:
        if animal.lower() in ['dog', 'cat', 'bird', 'fish']:
            endothermic.append(animal)
        elif animal.lower() in ['snake', 'lizard', 'frog']:
            ectothermic.append(animal)

    return {'endothermic': endothermic, 'ectothermic': ectothermic}

if __name__ == '__main__':
    animals = ['Dog', 'Cat', 'Bird', 'Fish', 'Snake', 'Lizard', 'Frog']
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)