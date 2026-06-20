import csv
import io

def calculate_average_weight(csv_content):
    weights = []
    reader = csv.reader(io.StringIO(csv_content))
    header = next(reader, None)
    for row in reader:
        if not row:
            continue
        for item in row:
            item = item.strip()
            if not item:
                continue
            try:
                value = float(item)
                weights.append(value)
            except ValueError:
                continue
    if not weights:
        return 0.0
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_csv = """id,weight
1,50.5
2,60.0
3,invalid
4,55.5
5,70.0"""
    result = calculate_average_weight(sample_csv)
    print(result)