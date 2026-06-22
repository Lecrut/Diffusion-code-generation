import csv
import os
import tempfile

def calculate_average_weights(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    category_totals = {}
    category_counts = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row['category'].strip()
            try:
                weight = float(row['weight'].strip())
            except (ValueError, KeyError) as e:
                continue

            if category not in category_totals:
                category_totals[category] = 0.0
                category_counts[category] = 0

            category_totals[category] += weight
            category_counts[category] += 1

    averages = {}
    for category in category_totals:
        if category_counts[category] > 0:
            averages[category] = category_totals[category] / category_counts[category]
        else:
            averages[category] = 0.0

    return averages

if __name__ == '__main__':
    data = "category,weight\nFruits,1.5\nVegetables,2.0\nFruits,2.5\nVegetables,3.0\nFruits,3.0\nVegetables,2.0\n"

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp:
        tmp.write(data)
        tmp_path = tmp.name

    try:
        result = calculate_average_weights(tmp_path)
        print(result)
    finally:
        os.unlink(tmp_path)