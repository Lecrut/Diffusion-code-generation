import csv

def convert_weights(input_file, output_file):
    conversion_factors = {'kg': 2.20462, 'lbs': 1, 'oz': 0.0625}
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            weight_value = float(row['weight'])
            weight_unit = row['unit']
            new_weight = weight_value * conversion_factors.get(weight_unit, 1) / conversion_factors['lbs']
            row['weight'] = new_weight
            row['unit'] = 'lbs'
            writer.writerow(row)

if __name__ == '__main__':
    input_file = 'sample_input.csv'
    output_file = 'converted_output.csv'
    convert_weights(input_file, output_file)