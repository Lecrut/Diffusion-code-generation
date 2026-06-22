import csv

def convert_kg_to_lb(weight):
    return weight * 2.20462

def convert_oz_to_lb(weight):
    return weight * 0.0625

def convert_weight(value, unit):
    if unit == 'kg':
        return convert_kg_to_lb(value)
    elif unit == 'lbs':
        return value
    elif unit == 'oz':
        return convert_oz_to_lb(value)
    else:
        raise ValueError(f"Unsupported weight unit: {unit}")

def process_csv(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            name = row['name']
            weight_value = float(row['weight'])
            weight_unit = row['unit']
            
            new_weight = convert_weight(weight_value, weight_unit)
            new_row = {
                'name': name,
                'weight': new_weight,
                'unit': 'lbs'
            }
            writer.writerow(new_row)

if __name__ == '__main__':
    process_csv('sample_input.csv', 'output.csv')