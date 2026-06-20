import csv
from io import StringIO

def calculate_average_weights(csv_content):
    category_weights = {}
    file_obj = StringIO(csv_content)
    try:
        reader = csv.DictReader(file_obj)
        for row in reader:
            category = row['category']
            weight = float(row['weight'])
            if category not in category_weights:
                category_weights[category] = []
            category_weights[category].append(weight)
    finally:
        file_obj.close()
    
    averages = {}
    for category, weights in category_weights.items():
        if weights:
            averages[category] = sum(weights) / len(weights)
        else:
            averages[category] = 0.0
    
    return averages

if __name__ == '__main__':
    sample_csv = "category,weight\nA,10.0\nB,20.0\nA,30.0\nC,40.0\nB,60.0"
    result = calculate_average_weights(sample_csv)
    print(result)