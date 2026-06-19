import csv
from io import StringIO

def calculate_average_weight(csv_data):
    try:
        reader = csv.reader(StringIO(csv_data))
        total_weight = 0.0
        count = 0
        for row in reader:
            for weight_str in row:
                try:
                    weight = float(weight_str)
                    total_weight += weight
                    count += 1
                except ValueError:
                    continue
        if count == 0:
            return None
        return total_weight / count
    except Exception as e:
        return None

if __name__ == '__main__':
    sample_csv_data = """75.5,80,68.2,invalid,90"""
    average_weight = calculate_average_weight(sample_csv_data)
    print(average_weight)