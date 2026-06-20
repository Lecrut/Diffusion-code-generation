import csv
import io
from collections import defaultdict

def calculate_average_weights_by_category(csv_data):
    category_weights = defaultdict(list)
    csv_file = io.StringIO(csv_data)
    with csv_file as file_handle:
        reader = csv.DictReader(file_handle)
        for row in reader:
            category = row.get('category')
            weight_str = row.get('weight')
            if category is not None and weight_str is not None:
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

if __name__ == '__main__':
    sample_csv = """category,weight
Fruit,150
Fruit,200
Vegetable,120
Vegetable,180
Grain,300
Grain,250"""
    result = calculate_average_weights_by_category(sample_csv)
    print(result)