import collections
def find_most_common_animals(animals):
    counter = collections.Counter()
    for animal in animals:
        if isinstance(animal, str) and len(animal.strip()) > 0:
            normalized = animal.lower().strip()
            counter[normalized] += 1
    most_common_list = counter.most_common(1)[0][0] if counter else None
    return most_common_list
if __name__ == '__main__':
    sample_data = [
        "Lion", "Tiger", "Elephant", "Cat", 
        "Dog", "Bird", "Fish", "Monkey", 
        "Lion", "Tiger", "Elephant", "Cat", 
        "dog", "bird", "lion"
    ]
    result = find_most_common_animals(sample_data)
    print(f"The most common animal is: {result}")