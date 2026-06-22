import csv
import tempfile
import os

def calculate_average_weight(csv_content):
    weights = []
    lines = csv_content.strip().split('\n')
    reader = csv.reader(lines)
    
    for row in reader:
        if not row:
            continue
        for item in row:
            try:
                weight = float(item)
                weights.append(weight)
            except ValueError:
                continue
    
    if not weights:
        return 0.0
    
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_csv_content = """150.5
160.2
invalid
175.8
abc
180.0
145.5"""
    
    result = calculate_average_weight(sample_csv_content)
    print(result)