import csv
import io

def extract_weights_from_csv(csv_text):
    valid_weights = []
    stream = io.StringIO(csv_text)
    reader = csv.reader(stream)
    for row in reader:
        for cell in row:
            stripped = cell.strip()
            if not stripped:
                continue
            try:
                weight = float(stripped)
                valid_weights.append(weight)
            except ValueError:
                continue
    return valid_weights

def calculate_mean(values):
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    return total / count

def process_weight_data(csv_content):
    weights = extract_weights_from_csv(csv_content)
    average = calculate_mean(weights)
    return average

if __name__ == '__main__':
    sample_csv = """
Weight,Date
70.5,2023-01-01
68.2,2023-01-02
bad_value,2023-01-03
71.0,2023-01-04
"""
    result = process_weight_data(sample_csv)
    print(result)