import csv
import os

def calculate_average_weights(csv_content):
    if not csv_content:
        return {}
    
    reader = csv.DictReader(csv_content.splitlines())
    categories = {}
    
    for row in reader:
        category = row.get('category', '').strip()
        weight_str = row.get('weight', '').strip()
        
        if not category or not weight_str:
            continue
            
        try:
            weight = float(weight_str)
        except ValueError:
            continue
            
        if category not in categories:
            categories[category] = []
        categories[category].append(weight)
        
    averages = {}
    for category, weights in categories.items():
        if weights:
            averages[category] = sum(weights) / len(weights)
            
    return averages

if __name__ == '__main__':
    sample_csv_data = "category,weight\nfruit,10\nfruit,20\nvegetable,5\nvegetable,15"
    result = calculate_average_weights(sample_csv_data)
    print(result)