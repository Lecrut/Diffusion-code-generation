import csv
import os
import tempfile

def scale_volumes(input_path, output_path, scale_factor):
    with open(input_path, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = ['Item', 'Scaled_Volume']
        with open(output_path, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                item_name = row['Item']
                volume = float(row['Volume'])
                scaled_volume = volume * scale_factor
                writer.writerow({
                    'Item': item_name,
                    'Scaled_Volume': scaled_volume
                })
    return output_path

if __name__ == '__main__':
    sample_items = ['Apple', 'Banana', 'Cherry']
    sample_volumes = [10.5, 20.0, 15.75]
    scale_factor = 2.5

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as temp_input:
        writer = csv.writer(temp_input)
        writer.writerow(['Item', 'Volume'])
        for item, volume in zip(sample_items, sample_volumes):
            writer.writerow([item, volume])
        temp_input_path = temp_input.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as temp_output:
        temp_output_path = temp_output.name

    result_path = scale_volumes(temp_input_path, temp_output_path, scale_factor)

    with open(result_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['Item'], row['Scaled_Volume'])

    os.unlink(temp_input_path)
    os.unlink(temp_output_path)