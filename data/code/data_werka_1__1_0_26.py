import csv
from collections import defaultdict

def calculate_average_weights(file_content):
    weights_by_category = defaultdict(list)
    for row in file_content:
        category, weight = row.strip().split(',')
        weights_by_category[category].append(float(weight))
    average_weights = {category: sum(weights) / len(weights) for category, weights in weights_by_category.items()}
    return average_weights
if __name__ == '__main__':
    sample_csv_content = ['Category1,70', 'Category2,80', 'Category1,75', 'Category2,85', 'Category3,90']
    result = calculate_average_weights(sample_csv_content)
    print(result)