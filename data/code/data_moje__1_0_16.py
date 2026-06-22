import csv
import io
from collections import defaultdict

def calculate_average_weight_by_category(csv_content):
    category_weights = defaultdict(list)
    reader = csv.DictReader(io.StringIO(csv_content))
    for row in reader:
        category = row.get('category', 'Unknown')
        try:
            weight = float(row.get('weight', 0))
            category_weights[category].append(weight)
        except ValueError:
            continue

    averages = {}
    for category, weights in category_weights.items():
        if weights:
            averages[category] = sum(weights) / len(weights)
        else:
            averages[category] = 0.0

    return averages

if __name__ == '__main__':
    sample_csv = """category,weight
fruit,1.5
vegetable,0.8
fruit,2.0
vegetable,1.2
grain,0.5
fruit,1.8
"""
    result = calculate_average_weight_by_category(sample_csv)
    print(result)