import csv
import os

def convert_celsius_to_fahrenheit(input_path, output_path):
    with open(input_path, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = []
        for row in reader:
            celsius = float(row['celsius'])
            fahrenheit = (celsius * 9 / 5) + 32
            row['fahrenheit'] = fahrenheit
            rows.append(row)
    with open(output_path, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames + ['fahrenheit'])
        writer.writeheader()
        writer.writerows(rows)
    return rows

if __name__ == '__main__':
    input_data = [
        {'celsius': '0'},
        {'celsius': '100'},
        {'celsius': '37'}
    ]
    input_file = 'temp_input.csv'
    output_file = 'temp_output.csv'
    with open(input_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['celsius'])
        writer.writeheader()
        writer.writerows(input_data)
    try:
        result = convert_celsius_to_fahrenheit(input_file, output_file)
        for row in result:
            print(row)
    finally:
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(output_file):
            os.remove(output_file)