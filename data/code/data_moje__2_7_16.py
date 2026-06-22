import csv
import os

def scale_volumes(input_path, output_path, scale_factor):
    with open(input_path, 'r', newline='') as infile, open(output_path, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        if fieldnames is None:
            return False
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            try:
                volume = float(row['Volume'])
                row['Scaled_Volume'] = volume * scale_factor
                writer.writerow(row)
            except (ValueError, KeyError) as e:
                continue
    return True

def create_sample_data(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Item', 'Volume'])
        writer.writerow(['Widget', '10.0'])
        writer.writerow(['Gadget', '25.5'])
        writer.writerow(['Doohickey', '5.0'])

if __name__ == '__main__':
    sample_input = 'sample_input.csv'
    sample_output = 'sample_output.csv'
    sample_factor = 2.0

    if os.path.exists(sample_output):
        os.remove(sample_output)

    create_sample_data(sample_input)

    success = scale_volumes(sample_input, sample_output, sample_factor)

    if success:
        with open(sample_output, 'r') as f:
            content = f.read()
        print(content)
    else:
        print("Error processing file")