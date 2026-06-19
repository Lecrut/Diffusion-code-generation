import csv
from collections import defaultdict

def calculate_average_weights(file_content):
    weights_by_category = defaultdict(list)
    for line in file_content.splitlines():
        category, weight_str = line.split(',')
        weight = float(weight_str)
        weights_by_category[category].append(weight)
    average_weights = {category: sum(weights) / len(weights) for category, weights in weights_by_category.items()}
    return average_weights
if __name__ == '__main__':
    sample_csv_content = 'Category,Weight\nFruits,1.2\nFruits,1.5\nVegetables,0.8\nVegetables,1.0\nDairy,1.0\nDairy,1.2'
    average_weights = calculate_average_weights(sample_csv_content)
    print(average_weights)