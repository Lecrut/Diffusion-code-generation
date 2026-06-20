import csv
import io

def calculate_average_weight(csv_content):
    weights = []
    csv_file = io.StringIO(csv_content)
    reader = csv.reader(csv_file)
    for row in reader:
        if not row:
            continue
        for value in row:
            stripped = value.strip()
            if not stripped:
                continue
            try:
                weight = float(stripped)
                weights.append(weight)
            except ValueError:
                continue
    if not weights:
        return 0.0
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_csv = """
weight_kg
70.5
65.2
invalid
80.1
75.0
"""
    result = calculate_average_weight(sample_csv)
    print(result)