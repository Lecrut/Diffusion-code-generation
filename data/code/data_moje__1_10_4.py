import csv
import io

def calculate_average_weight(csv_data, weight_column='weight'):
    if isinstance(csv_data, str):
        reader = csv.DictReader(io.StringIO(csv_data))
    else:
        reader = csv.DictReader(csv_data)
    valid_weights = []
    for row in reader:
        if weight_column not in row:
            continue
        value = row[weight_column]
        if value is None or value == '':
            continue
        try:
            weight = float(value)
            valid_weights.append(weight)
        except (ValueError, TypeError):
            continue
    if not valid_weights:
        return None
    average = sum(valid_weights) / len(valid_weights)
    return average

def process_weight_csv(file_content, weight_column='weight'):
    if isinstance(file_content, str):
        csv_file = io.StringIO(file_content)
    else:
        csv_file = file_content
    valid_weights = []
    error_count = 0
    error_rows = []
    try:
        reader = csv.DictReader(csv_file)
        for row_num, row in enumerate(reader, start=2):
            if weight_column not in row:
                continue
            value = row[weight_column]
            if value is None or value.strip() == '':
                continue
            try:
                weight = float(value)
                valid_weights.append(weight)
            except (ValueError, TypeError):
                error_count += 1
                error_rows.append(row_num)
    except csv.Error:
        return {'average': None, 'count': 0, 'errors': 'CSV parsing error', 'error_count': -1}
    if not valid_weights:
        return {'average': None, 'count': 0, 'errors': 'No valid weight values found', 'error_count': error_count}
    average = sum(valid_weights) / len(valid_weights)
    return {'average': average, 'count': len(valid_weights), 'errors': f'{error_count} non-numeric entries ignored', 'error_count': error_count}
if __name__ == '__main__':
    sample_csv = 'name,weight,age\nAlice,65.5,30\nBob,invalid,25\nCharlie,72.3,35\n,58.1,28\nEve,80.0,40\nFrank,,33\nGrace,abc,27\nHeidi,77.8,31\nIvan,69.2,34\nJudy,nonumber,29'
    result = process_weight_csv(sample_csv)
    print(result['average'])
    print(result['count'])
    print(result['errors'])