import csv
import io
from collections import defaultdict

def calculate_average_weights(csv_content):
    category_weights = defaultdict(list)
    reader = csv.DictReader(io.StringIO(csv_content))
    for row in reader:
        category = row['category']
        weight = float(row['weight'])
        category_weights[category].append(weight)
    averages = {}
    for category, weights in category_weights.items():
        averages[category] = sum(weights) / len(weights)
    return averages
if __name__ == '__main__':
    sample_csv = 'category,weight\nfruit,150\nvegetable,200\nfruit,170\nvegetable,180\ndairy,300\nfruit,160\ndairy,280\nvegetable,220'
    result = calculate_average_weights(sample_csv)
    print(result)