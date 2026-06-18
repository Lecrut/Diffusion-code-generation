import collections
from typing import List
def find_most_common_animals(animal_list: List[str]) -> dict:
    counter = collections.Counter()
    for animal in animal_list:
        if isinstance(animal, str) and len(animal.strip()) > 0:
            normalized_name = animal.lower().strip()
            count = counter[normalized_name] + 1
            counter[normalized_name] = count
    return dict(counter.most_common(5))
if __name__ == '__main__':
    sample_data = [
        "Lion", "Tiger", "Elephant", "Cat", 
        "Dog", "Bird", "Lion", "Tiger", "Monkey", 
        "Rabbit", "Snake", "Fish", "Cat", "Pig"
    ]
    result = find_most_common_animals(sample_data)
    print("Top 5 most common animals:")
    for animal, count in result.items():
        print(f"{animal}: {count}")