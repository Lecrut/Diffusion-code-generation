import collections
def find_most_common_animals(animal_list):
    counter = collections.Counter()
    for animal in animal_list:
        if isinstance(animal, str) and len(animal.strip()) > 0:
            cleaned_animal = animal.lower().strip()
            counter[cleaned_animal] += 1
    most_common_items = counter.most_common(1)[0]
    return {
        'animal': most_common_items[0][0],
        'count': most_common_items[0][1]
    }
if __name__ == '__main__':
    sample_data = [
        "Lion", "Tiger", "Elephant", "Cat", 
        "Dog", "Bird", "Fish", "Monkey", 
        "Cat", "dog", "CAT", "LION"
    ]
    result = find_most_common_animals(sample_data)
    print(f"The most common animal is '{result['animal']}' with {result['count']} occurrences.")