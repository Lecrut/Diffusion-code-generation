import csv
import io

def extract_numeric_weights(csv_text):
    weights = []
    reader = csv.reader(io.StringIO(csv_text))
    for row in reader:
        for cell in row:
            cleaned = cell.strip()
            if not cleaned:
                continue
            try:
                weight_value = float(cleaned)
                weights.append(weight_value)
            except ValueError:
                continue
    return weights

def compute_average(values):
    if not values:
        return 0.0
    total_sum = sum(values)
    count = len(values)
    return total_sum / count

def analyze_weights(csv_data):
    valid_weights = extract_numeric_weights(csv_data)
    average_weight = compute_average(valid_weights)
    return average_weight

if __name__ == '__main__':
    sample_csv = """
Name,Weight,Date
Alice,60.5,2023-01-01
Bob,invalid,2023-01-02
Charlie,75.0,2023-01-03
,,
David,80.2,2023-01-04
Eve,NaN,2023-01-05
"""
    result = analyze_weights(sample_csv)
    print(result)