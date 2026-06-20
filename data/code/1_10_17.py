import csv
import io

def calculate_average_weight(csv_content):
    lines = csv_content.strip().splitlines()
    reader = csv.reader(lines)
    weights = []
    for row in reader:
        for item in row:
            item = item.strip()
            if item:
                try:
                    weight = float(item)
                    weights.append(weight)
                except ValueError:
                    continue
    if not weights:
        return 0.0
    return sum(weights) / len(weights)
if __name__ == '__main__':
    sample_csv = 'weight1,weight2,weight3\n70.5,68.2,invalid\n80.1,,75.3\nabc,90.0,85.5'
    result = calculate_average_weight(sample_csv)
    print(result)