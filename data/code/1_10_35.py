import csv
from io import StringIO

def calculate_average_weight(csv_data):
    weights = []
    for row in csv.reader(StringIO(csv_data)):
        try:
            weight = float(row[0])
            weights.append(weight)
        except ValueError:
            continue
    if not weights:
        return 0.0
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_csv_data = """70.5\n80.2\ninvalid\n90.3\n100.0"""
    average_weight = calculate_average_weight(sample_csv_data)
    print(average_weight)