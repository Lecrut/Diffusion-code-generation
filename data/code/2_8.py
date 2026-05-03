import csv
def process_volumes(input_filename, output_filename, scale_factor):
    with open(input_filename, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if len(row) == 2:
                try:
                    item_name = row[0]
                    volume = float(row[1])
                    scaled_volume = volume * scale_factor
                    with open(output_filename, mode='w', newline='') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow([item_name, scaled_volume])
                except ValueError:
                    continue
            else:
                continue
if __name__ == '__main__':
    input_file = 'input.csv'
    output_file = 'output.csv'
    scale_factor = 2.5
    sample_data = [
        ['Apple', '10.0'],
        ['Banana', '5.5'],
        ['Orange', '12.0'],
        ['Grape', '8.0']
    ]
    with open(input_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
    process_volumes(input_file, output_file, scale_factor)