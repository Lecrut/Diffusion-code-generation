import csv
import io
import os

def calculate_average_weights_by_category(csv_content):
    weight_sums = {}
    count_sums = {}

    reader = csv.DictReader(io.StringIO(csv_content))
    
    for row in reader:
        try:
            category = row['category'].strip()
            weight = float(row['weight'])
        except (KeyError, ValueError, IndexError):
            continue

        if not category:
            continue

        if category not in weight_sums:
            weight_sums[category] = 0.0
            count_sums[category] = 0

        weight_sums[category] += weight
        count_sums[category] += 1

    results = {}
    for category in weight_sums:
        if count_sums[category] > 0:
            results[category] = weight_sums[category] / count_sums[category]

    return results

if __name__ == '__main__':
    sample_data = """category,weight
Fruit,10.5
Vegetable,5.2
Fruit,12.3
Meat,8.0
Vegetable,6.8
Fruit,9.7
Meat,10.0
Fruit,11.0"""

    averages = calculate_average_weights_by_category(sample_data)

    for category, avg in averages.items():
        print(f"{category}: {avg:.2f}")