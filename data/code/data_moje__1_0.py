import csv
import os
import tempfile

def calculate_average_weights(file_path):
    if not os.path.exists(file_path):
        return {}
    
    category_sums = {}
    category_counts = {}
    
    with open(file_path, 'newline', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row.get('category')
            weight_str = row.get('weight')
            
            if category is None or weight_str is None:
                continue
                
            try:
                weight = float(weight_str)
            except ValueError:
                continue
            
            if category in category_sums:
                category_sums[category] += weight
                category_counts[category] += 1
            else:
                category_sums[category] = weight
                category_counts[category] = 1
                
    averages = {}
    for category in category_sums:
        if category_counts[category] > 0:
            averages[category] = category_sums[category] / category_counts[category]
            
    return averages

def create_sample_csv():
    fd, path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'category', 'weight'])
        writer.writerow([1, 'A', '10.0'])
        writer.writerow([2, 'A', '20.0'])
        writer.writerow([3, 'B', '30.0'])
        writer.writerow([4, 'B', '40.0'])
        writer.writerow([5, 'C', '50.0'])
    return path

if __name__ == '__main__':
    sample_file = create_sample_csv()
    result = calculate_average_weights(sample_file)
    print(result)
    os.unlink(sample_file)