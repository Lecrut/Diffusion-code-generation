import csv
from typing import List

def calculate_average_weight(file_content: str) -> float:
    weights = []
    for line in file_content.splitlines():
        try:
            weight = float(line.strip())
            weights.append(weight)
        except ValueError:
            continue
    if not weights:
        return 0.0
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_csv_data = """75.5\n80.2\n78.9\nabc\n60.3"""
    average_weight = calculate_average_weight(sample_csv_data)
    print(average_weight)