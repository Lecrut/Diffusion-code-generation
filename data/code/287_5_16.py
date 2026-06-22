import csv

def convert_weights(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            weight = float(row['weight'])
            unit = row['unit'].lower()
            
            if unit == 'kg':
                weight *= 2.20462
            elif unit == 'oz':
                weight /= 16
            
            row['weight'] = f"{weight:.2f} lbs"
            writer.writerow(row)

if __name__ == '__main__':
    convert_weights('sample_input.csv', 'output.csv')