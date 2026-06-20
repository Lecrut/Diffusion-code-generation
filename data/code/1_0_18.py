import csv
import tempfile
import os
from collections import defaultdict

def calculate_average_weights_by_category(file_path):
    category_weights = defaultdict(list)

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row.get('category', '').strip()
            weight_str = row.get('weight', '').strip()

            if category and weight_str:
                try:
                    weight = float(weight_str)
                    category_weights[category].append(weight)
                except ValueError:
                    continue

    averages = {}
    for category, weights in category_weights.items():
        if weights:
            averages[category] = sum(weights) / len(weights)

    return averages

def main():
    sample_data = [
        ["category", "weight"],
        ["fruit", "1.5"],
        ["vegetable", "0.8"],
        ["fruit", "2.0"],
        ["dairy", "0.5"],
        ["vegetable", "1.2"],
        ["fruit", "1.0"],
        ["dairy", "0.7"],
    ]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as tmpfile:
        writer = csv.writer(tmpfile)
        writer.writerows(sample_data)
        tmpfile_path = tmpfile.name

    try:
        result = calculate_average_weights_by_category(tmpfile_path)
        print(result)
    finally:
        os.unlink(tmpfile_path)

if __name__ == '__main__':
    main()