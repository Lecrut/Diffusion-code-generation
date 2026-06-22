import csv
import os
import tempfile

def calculate_average_weights(file_path):
    weights_by_category = {}
    counts_by_category = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['category']
            try:
                weight = float(row['weight'])
            except (ValueError, KeyError):
                continue
            
            if category not in weights_by_category:
                weights_by_category[category] = 0.0
                counts_by_category[category] = 0
            
            weights_by_category[category] += weight
            counts_by_category[category] += 1

    averages = {}
    for category in weights_by_category:
        if counts_by_category[category] > 0:
            averages[category] = weights_by_category[category] / counts_by_category[category]
    
    return averages

if __name__ == '__main__':
    sample_csv_content = """category,weight
A,10
B,20
A,30
B,40
A,50"""

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8') as tmp:
        tmp.write(sample_csv_content)
        tmp_path = tmp.name

    try:
        result = calculate_average_weights(tmp_path)
        print(result)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)