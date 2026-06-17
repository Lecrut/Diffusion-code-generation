import json
from collections import Counter
def process_animal_data(animals):
    counts = Counter(animals)
    most_common_species = []
    max_count = 0
    for animal in animals:
        if counts[animal] > max_count:
            max_count = counts[animal]
    for animal, count in counts.items():
        if count == max_count and len(most_common_species) < 1:
            most_common_species.append(animal)
    return {'species': most_common_species, 'count': max_count}
def main():
    sample_data = [
        "dog", "cat", "fish", "bird", "dog", 
        "hamster", "rabbit", "snake", "lizard", "insect"
    ] * 10 + ["dog"] * 5
    result = process_animal_data(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)
if __name__ == '__main__':
    main()