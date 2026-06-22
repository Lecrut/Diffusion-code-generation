import csv
import tempfile
import os

def calculate_average_weight_by_category(file_path):
    category_weights = {}
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['category']
            try:
                weight = float(row['weight'])
            except (ValueError, KeyError):
                continue
            if category not in category_weights:
                category_weights[category] = []
            category_weights[category].append(weight)
    averages = {}
    for category, weights in category_weights.items():
        if weights:
            averages[category] = sum(weights) / len(weights)
    return averages

def create_sample_csv(file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['category', 'weight'])
        writer.writerow(['fruit', 0.5])
        writer.writerow(['fruit', 0.8])
        writer.writerow(['vegetable', 0.3])
        writer.writerow(['vegetable', 0.6])
        writer.writerow(['meat', 1.2])
        writer.writerow(['meat', 1.5])
        writer.writerow(['grain', 0.2])

if __name__ == '__main__':
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp:
        tmp_path = tmp.name
    create_sample_csv(tmp_path)
    result = calculate_average_weight_by_category(tmp_path)
    print(result)
    os.unlink(tmp_path)