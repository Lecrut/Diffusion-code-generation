import csv

def calculate_average_weight(file_content):
    weights = []
    for row in file_content:
        try:
            weight = float(row[0])
            weights.append(weight)
        except ValueError:
            continue
    if not weights:
        return 0.0
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_csv_content = [
        ['70.5'],
        ['68.2'],
        ['invalid'],
        ['72.3']
    ]
    average_weight = calculate_average_weight(sample_csv_content)
    print(average_weight)