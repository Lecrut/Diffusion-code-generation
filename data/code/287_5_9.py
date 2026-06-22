import csv

def convert_to_pounds(weight_value, weight_unit):
    conversion_factors = {'kg': 2.20462, 'lbs': 1, 'oz': 0.0625}
    return weight_value * conversion_factors.get(weight_unit, 1)

def process_csv(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            weight_value = float(row['weight'])
            weight_unit = row['unit']
            new_weight = convert_to_pounds(weight_value, weight_unit)
            row['weight'] = new_weight
            row['unit'] = 'lbs'
            writer.writerow(row)

if __name__ == '__main__':
    process_csv('sample_input.csv', 'output.csv')