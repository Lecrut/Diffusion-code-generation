import csv
from collections import defaultdict

def calculate_average_weight_by_category(csv_data):
    category_sums = defaultdict(float)
    category_counts = defaultdict(int)

    for row in csv_data:
        category = row['category']
        weight = float(row['weight'])
        category_sums[category] += weight
        category_counts[category] += 1

    average_weights = {category: sums / counts for category, sums in category_sums.items() for category, counts in category_counts.items() if counts > 0}
    return average_weights

if __name__ == '__main__':
    sample_csv_data = [
        {'category': 'fruits', 'weight': '1.2'},
        {'category': 'vegetables', 'weight': '0.5'},
        {'category': 'fruits', 'weight': '1.8'},
        {'category': 'dairy', 'weight': '2.0'},
        {'category': 'vegetables', 'weight': '0.7'}
    ]

    average_weights = calculate_average_weight_by_category(sample_csv_data)
    print(average_weights)