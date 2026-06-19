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
    sample_csv_data = """170.5,John Doe
                      180.2,Jane Smith
                      abc,Invalid Entry
                      165.4,Alice Johnson"""
    
    file_content = csv.reader(sample_csv_data.splitlines())
    average_weight = calculate_average_weight(file_content)
    print(average_weight)