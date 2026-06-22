import csv
import io

def calculate_average_weight_per_category(csv_content):
    lines = csv_content.strip().splitlines()
    reader = csv.DictReader(lines)
    category_weights = {}
    
    for row in reader:
        try:
            category = row['category'].strip()
            weight = float(row['weight'])
            if category not in category_weights:
                category_weights[category] = []
            category_weights[category].append(weight)
        except (KeyError, ValueError):
            continue
    
    averages = {}
    for category, weights in category_weights.items():
        if weights:
            averages[category] = sum(weights) / len(weights)
    
    return averages

if __name__ == '__main__':
    sample_csv_data = """category,weight
fruits,1.5
vegetables,2.0
fruits,3.5
vegetables,4.0
meat,10.0
meat,12.0
fruits,2.0"""
    
    result = calculate_average_weight_per_category(sample_csv_data)
    print(result)