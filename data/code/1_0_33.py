import csv
from collections import defaultdict

def calculate_average_weights(file_content):
    weights_by_category = defaultdict(list)
    reader = csv.DictReader(file_content.splitlines())
    
    for row in reader:
        category = row['category']
        weight = float(row['weight'])
        weights_by_category[category].append(weight)
    
    average_weights = {category: sum(weights) / len(weights) for category, weights in weights_by_category.items()}
    return average_weights

if __name__ == '__main__':
    sample_csv_content = """category,weight
fruits,1.2
vegetables,0.8
fruits,1.5
vegetables,0.9
meats,2.0"""
    
    result = calculate_average_weights(sample_csv_content)
    print(result)