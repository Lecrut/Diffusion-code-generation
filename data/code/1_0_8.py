import csv
import io

def calculate_average_weights_by_category(csv_content):
    categories = {}
    lines = csv_content.strip().splitlines()
    reader = csv.reader(lines)
    next(reader)
    
    for row in reader:
        if len(row) < 2:
            continue
        try:
            category = row[0].strip()
            weight = float(row[1].strip())
            if category not in categories:
                categories[category] = []
            categories[category].append(weight)
        except ValueError:
            continue
            
    results = {}
    for category, weights in categories.items():
        if weights:
            results[category] = sum(weights) / len(weights)
            
    return results

if __name__ == '__main__':
    sample_csv = """Category,Weight
Apples,1.2
Oranges,0.8
Apples,1.5
Bananas,0.4
Oranges,1.1
Bananas,0.6
"""
    averages = calculate_average_weights_by_category(sample_csv)
    for category, avg in averages.items():
        print(f"{category}: {avg:.2f}")