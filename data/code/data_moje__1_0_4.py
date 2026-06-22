import csv
import io
import os

def calculate_average_weights_by_category(csv_content):
    category_weights = {}
    
    lines = csv_content.strip().splitlines()
    reader = csv.DictReader(lines)
    
    for row in reader:
        category = row['category']
        weight = float(row['weight'])
        
        if category not in category_weights:
            category_weights[category] = []
        category_weights[category].append(weight)
    
    averages = {}
    for category, weights in category_weights.items():
        total = sum(weights)
        count = len(weights)
        averages[category] = total / count
    
    return averages

if __name__ == '__main__':
    sample_csv_data = """id,category,weight
1,Electronics,2.5
2,Books,0.3
3,Electronics,3.2
4,Books,0.5
5,Clothing,0.8
6,Electronics,1.8
7,Clothing,1.2
8,Books,0.4"""
    
    result = calculate_average_weights_by_category(sample_csv_data)
    
    for category, avg_weight in result.items():
        print(f"{category}: {avg_weight:.2f}")