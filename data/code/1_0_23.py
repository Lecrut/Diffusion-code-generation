import csv
from collections import defaultdict

def calculate_average_weights(csv_data):
    category_sums = defaultdict(float)
    category_counts = defaultdict(int)
    
    for row in csv.reader(csv_data.splitlines()):
        if len(row) < 2:
            continue
        category, weight = row[0], float(row[1])
        category_sums[category] += weight
        category_counts[category] += 1
    
    averages = {category: total / count for category, total in category_sums.items() for count in category_counts.values() if count != 0}
    return averages

if __name__ == '__main__':
    sample_csv_data = """Category,Weight
Apples,2.5
Oranges,3.0
Bananas,1.5
Apples,2.0
Oranges,2.8"""
    
    average_weights = calculate_average_weights(sample_csv_data)
    print(average_weights)