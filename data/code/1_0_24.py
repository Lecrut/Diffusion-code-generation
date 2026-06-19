import csv
from collections import defaultdict

def calculate_average_weights(csv_data):
    weights_by_category = defaultdict(list)
    
    for row in csv.DictReader(csv_data.splitlines()):
        category = row['Category']
        weight = float(row['Weight'])
        weights_by_category[category].append(weight)
    
    average_weights = {category: sum(weights) / len(weights) for category, weights in weights_by_category.items()}
    return average_weights

if __name__ == '__main__':
    sample_csv_data = """Category,Weight
Fruit,1.2
Fruit,1.5
Vegetable,0.8
Vegetable,0.9
Dairy,1.0
Dairy,1.1"""
    
    average_weights = calculate_average_weights(sample_csv_data)
    print(average_weights)