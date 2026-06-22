import csv

def validate_input(file_path):
    with open(file_path, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if 'weight' not in row or 'unit' not in row:
                raise ValueError("CSV must contain 'weight' and 'unit' columns")
            if row['unit'] not in ['kg', 'lbs', 'oz']:
                raise ValueError("Invalid unit. Must be 'kg', 'lbs', or 'oz'")

def convert_weight(value, from_unit):
    conversion_factors = {'kg': 2.20462, 'lbs': 1, 'oz': 0.0625}
    return value * conversion_factors[from_unit]

def write_output(file_path, data):
    with open(file_path, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['name', 'weight'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def convert_weights(input_file, output_file):
    validate_input(input_file)
    data = []
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            new_weight = convert_weight(float(row['weight']), row['unit'])
            data.append({'name': row['name'], 'weight': new_weight})
    write_output(output_file, data)

if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'output.csv'
    convert_weights(input_csv, output_csv)