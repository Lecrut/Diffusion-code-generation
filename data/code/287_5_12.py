import csv

KG_TO_LB = 2.20462
LBS_TO_KG = 0.453592

def convert_weight(value, from_unit):
    if from_unit == "kg":
        return value * KG_TO_LB
    elif from_unit == "lbs":
        return value
    elif from_unit == "oz":
        return value / 16 * KG_TO_LB
    else:
        raise ValueError(f"Unsupported unit: {from_unit}")

def convert_weights(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            weight_value = float(row['weight'])
            from_unit = row['unit']
            new_weight = convert_weight(weight_value, from_unit)
            row['weight'] = new_weight
            row['unit'] = 'lbs'
            writer.writerow(row)

if __name__ == '__main__':
    convert_weights('sample_input.csv', 'output.csv')