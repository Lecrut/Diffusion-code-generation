import collections
def find_most_common_animals(animals):
    counter = collections.Counter()
    for animal in animals:
        if isinstance(animal, str) and len(animal.strip()) > 0:
            normalized = animal.lower().strip()
            counter[normalized] += 1
    return counter.most_common(1)[0][0], counter.most_common(1)[0][1]
if __name__ == '__main__':
    sample_data = [
        "Lion", "Tiger", "Elephant", "Cat", 
        "Dog", "Monkey", "Zebra", "Bear", 
        "Wolf", "Fox", "Rabbit", "Horse", 
        "Cow", "Pig", "Sheep", "Goat",
        "Lion", "Tiger", "Elephant", "Cat", 
        "Dog", "Monkey", "Zebra", "Bear"
    ]
    most_common, count = find_most_common_animals(sample_data)
    print(f"The most common animal is '{most_common}' with {count} occurrences.")