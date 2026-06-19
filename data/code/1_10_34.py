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
    sample_csv_content = """70.5
82.3
65.4
invalid
90.1"""
    average_weight = calculate_average_weight(sample_csv_content)
    print(average_weight)