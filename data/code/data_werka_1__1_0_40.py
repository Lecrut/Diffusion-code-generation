import csv
from collections import defaultdict

def calculate_average_weights(file_content):
    weights_by_category = defaultdict(list)
    reader = csv.DictReader(file_content.splitlines())
    for row in reader:
        category = row['Category']
        weight = float(row['Weight'])
        weights_by_category[category].append(weight)
    average_weights = {category: sum(weights) / len(weights) for category, weights in weights_by_category.items()}
    return average_weights
if __name__ == '__main__':
    sample_csv_content = 'Category,Weight\nFruit,1.2\nFruit,1.5\nVegetable,0.8\nVegetable,0.9\nDairy,1.0\nDairy,1.1'
    average_weights = calculate_average_weights(sample_csv_content)
    print(average_weights)