import csv

def calculate_average_weight(file_content):
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
    sample_csv_content = """75.5
82.3
invalid
69.8
74.0"""
    average_weight = calculate_average_weight(sample_csv_content)
    print(f"Average Weight: {average_weight}")