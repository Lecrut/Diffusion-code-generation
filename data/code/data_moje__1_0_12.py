import csv
import os
import tempfile

def calculate_average_weights_by_category(csv_file_path):
    category_weights = {}
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'category' not in row or 'weight' not in row:
                    continue
                category = row['category'].strip()
                weight_str = row['weight'].strip()
                if not category or not weight_str:
                    continue
                try:
                    weight = float(weight_str)
                    if category not in category_weights:
                        category_weights[category] = []
                    category_weights[category].append(weight)
                except ValueError:
                    continue
    except FileNotFoundError:
        return {}
    except Exception:
        return {}
    
    averages = {}
    for category, weights in category_weights.items():
        if weights:
            averages[category] = sum(weights) / len(weights)
        else:
            averages[category] = 0.0
    return averages

def create_sample_csv(content, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    sample_data = """category,weight
A,10.5
B,20.0
A,14.5
C,30.0
B,22.5
A,15.0
C,32.5
B,17.5"""
    
    temp_dir = tempfile.gettempdir()
    sample_file_path = os.path.join(temp_dir, 'sample_weights.csv')
    
    create_sample_csv(sample_data, sample_file_path)
    
    result = calculate_average_weights_by_category(sample_file_path)
    
    for category, avg in sorted(result.items()):
        print(f"Category {category}: Average Weight = {avg}")