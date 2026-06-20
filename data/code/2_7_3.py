import csv
import os

def scale_volumes(input_path, output_path, scale_factor):
    with open(input_path, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        rows = []
        for row in reader:
            item_name = row['item']
            volume = float(row['volume'])
            scaled_volume = volume * scale_factor
            rows.append({'item': item_name, 'scaled_volume': scaled_volume})
    
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['item', 'scaled_volume'])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    
    return rows

if __name__ == '__main__':
    input_file = 'items_input.csv'
    output_file = 'items_output.csv'
    
    sample_data = [
        {'item': 'apple', 'volume': 10.5},
        {'item': 'banana', 'volume': 20.0},
        {'item': 'cherry', 'volume': 5.25}
    ]
    
    with open(input_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['item', 'volume'])
        writer.writeheader()
        for row in sample_data:
            writer.writerow(row)
    
    result = scale_volumes(input_file, output_file, 2.5)
    print(result)