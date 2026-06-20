import csv
import io

def calculate_average_weight(csv_content):
    weights = []
    reader = csv.reader(io.StringIO(csv_content))
    header_skipped = False
    for row in reader:
        if not row:
            continue
        if not header_skipped:
            try:
                float(row[0])
            except ValueError:
                header_skipped = True
                continue
            header_skipped = False
        for cell in row:
            cell = cell.strip()
            if not cell:
                continue
            try:
                weight = float(cell)
                weights.append(weight)
            except ValueError:
                continue
    if not weights:
        return 0.0
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_csv_data = """weight
70.5
80.2
invalid
65.0
75.8
abc
90.1
"""
    average = calculate_average_weight(sample_csv_data)
    print(average)