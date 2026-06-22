import csv
from collections import defaultdict

def calculate_average_weights(csv_content: str) -> dict[str, float]:
    categories = defaultdict(list)
    lines = csv_content.strip().splitlines()
    if not lines:
        return {}
    reader = csv.DictReader(lines)
    for row in reader:
        category = row['category']
        weight = float(row['weight'])
        categories[category].append(weight)
    averages = {}
    for category, weights in categories.items():
        if weights:
            averages[category] = sum(weights) / len(weights)
    return averages

if __name__ == '__main__':
    sample_csv = """category,weight
Fruit,10
Vegetable,20
Fruit,15
Vegetable,25
Fruit,5
Vegetable,10
"""
    result = calculate_average_weights(sample_csv)
    print(result)