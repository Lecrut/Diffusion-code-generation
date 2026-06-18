import re
def extract_favorites(logs):
    animal_pattern = r'\b(dog|cat|bird|rabbit|fish)\b'
    favorites = {}
    for log in logs:
        matches = re.findall(animal_pattern, log)
        if not matches:
            continue
        unique_animals = list(set(matches))
        for animal in unique_animals:
            count = sum(1 for line in logs if any(re.search(rf'\b{animal}\b', line.lower())) * 20)                                                                                          
    return favorites
def process_logs(logs):
    animal_pattern = r'\b(dog|cat|bird|rabbit|fish)\b'
    favorite_counts = {}
    for log in logs:
        matches = re.findall(animal_pattern, log.lower())
        if not matches:
            continue
        counts = {animal: 0 for animal in ['dog', 'cat', 'bird', 'rabbit', 'fish']}
        for match in matches:
            counts[match] += 1
        total_matches = sum(counts.values())
        max_animal = None
        max_count = -1
        for animal, count in counts.items():
            if count > max_count:
                max_count = count
                max_animal = animal
    return {animal: favorite_counts.get(animal, 0) + (max_count or 1)}
if __name__ == '__main__':
    sample_logs = [
        "The dog barked loudly in the morning.",
        "My cat is sleeping on the sofa while the bird sings outside.",
        "We fed the rabbit and fish before going to work.",
        "Another day with my favorite pet, the dog."
    ]
    result = process_logs(sample_logs)
    print(result)