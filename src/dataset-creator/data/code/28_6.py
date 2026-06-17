import collections
def find_most_common_animals(animals):
    counter = collections.Counter()
    for animal in animals:
        if isinstance(animal, str) and len(animal.strip()) > 0:
            cleaned = animal.lower().strip()
            counter[cleaned] += 1
    return counter.most_common(1)[0][0], counter.most_common(1)[0][1]
if __name__ == '__main__':
    sample_data = [
        "lion", "tiger", "elephant", "dog", "cat", 
        "bird", "fish", "snake", "lizard", "mouse",
        "rabbit", "hamster", "guinea pig", "ferret", "otter",
        "bear", "wolf", "fox", "deer", "moose",
        "lion", "tiger", "elephant", "dog", "cat", 
        "bird", "fish", "snake", "lizard", "mouse",
        "rabbit", "hamster", "guinea pig", "ferret", "otter",
        "bear", "wolf", "fox", "deer", "moose"
    ]
    most_common, count = find_most_common_animals(sample_data)
    print(f"The most common animal is {most_common} with {count} occurrences.")