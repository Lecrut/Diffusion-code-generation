import csv
import io

def parse_weight_entry(raw_value):
    cleaned = raw_value.strip()
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None

def extract_valid_weights_from_stream(stream):
    valid_weights = []
    reader = csv.reader(stream)
    for row in reader:
        for cell in row:
            parsed = parse_weight_entry(cell)
            if parsed is not None:
                valid_weights.append(parsed)
    return valid_weights

def compute_mean_weight(weights):
    if not weights:
        return 0.0
    total = sum(weights)
    count = len(weights)
    return total / count

class WeightProcessor:
    def __init__(self, raw_csv_data):
        self.raw_csv_data = raw_csv_data

    def run_analysis(self):
        stream = io.StringIO(self.raw_csv_data)
        weights = extract_valid_weights_from_stream(stream)
        average = compute_mean_weight(weights)
        return average

if __name__ == '__main__':
    sample_data = """weight
10.5
invalid
15.2
20.0
bad_entry
8.3
"""
    processor = WeightProcessor(sample_data)
    result = processor.run_analysis()
    print(result)