import re
from collections import Counter
def extract_animal_mentions(text):
    animal_pattern = r'\b(cat|dog|bird|rabbit|horse|cow|pig|sheep|goat|fish)\s*(?:love|likes|has|is)'
    matches = []
    for match in re.finditer(animal_pattern, text, re.IGNORECASE):
        animals = [m.group(1).lower() for m in match.groups()]
        if not animals:
            continue
        for animal in set(animals):
            matches.append(animal)
    return Counter(matches)
def process_logs(logs):
    total_counts = {}
    for log_text in logs:
        counts = extract_animal_mentions(log_text)
        for animal, count in counts.items():
            if animal not in total_counts or total_counts[animal] < count:
                total_counts[animal] = count
    return dict(total_counts)
if __name__ == '__main__':
    sample_logs = [
        "John loves cats and dogs.",
        "Sarah has a pet rabbit that she really likes.",
        "The farm is full of cows, pigs, and sheep."
    ]
    result = process_logs(sample_logs)
    print(result)