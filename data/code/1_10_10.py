import csv
import io

def calculate_average_weight(csv_content):
    reader = csv.reader(io.StringIO(csv_content))
    weights = []
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
    sample_csv = 'weight,description\n70.5,adult\n65.2,teen\nabc,invalid\n80.1,man\n,empty\n55.0,girl'
    average = calculate_average_weight(sample_csv)
    print(average)