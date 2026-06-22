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
    sample_csv_content = 'Category,Weight\nFruits,1.2\nFruits,0.8\nVegetables,0.5\nVegetables,0.7\nGrains,0.3\nGrains,0.4'
    average_weights = calculate_average_weights(sample_csv_content)
    print(average_weights)