import csv
import io
from collections import defaultdict

def calculate_average_weights(csv_content):
    weight_sums = defaultdict(float)
    weight_counts = defaultdict(int)

    file_like_object = io.StringIO(csv_content)
    reader = csv.DictReader(file_like_object)

    for row in reader:
        category = row.get('category')
        weight_str = row.get('weight')

        if category is not None and weight_str is not None:
            try:
                weight = float(weight_str)
                weight_sums[category] += weight
                weight_counts[category] += 1
            except ValueError:
                continue

    averages = {}
    for category in weight_sums:
        if weight_counts[category] > 0:
            averages[category] = weight_sums[category] / weight_counts[category]

    return averages

if __name__ == '__main__':
    sample_csv = """category,weight
A,10.5
B,20.0
A,15.5
B,25.0
C,30.0
A,12.0
"""
    result = calculate_average_weights(sample_csv)
    print(result)