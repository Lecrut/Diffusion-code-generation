import csv
import os

def scale_volumes(input_file, output_file, scale_factor):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            for row in reader:
                if len(row) >= 2:
                    item_name = row[0]
                    try:
                        volume = float(row[1])
                        scaled_volume = volume * scale_factor
                        writer.writerow([item_name, scaled_volume])
                    except ValueError:
                        continue
                else:
                    continue
    return output_file
if __name__ == '__main__':
    input_file = 'items.csv'
    output_file = 'scaled_items.csv'
    scale_factor = 2.5
    with open(input_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Item', 'Volume'])
        writer.writerow(['Item1', 10.0])
        writer.writerow(['Item2', 20.0])
        writer.writerow(['Item3', 30.0])
    result = scale_volumes(input_file, output_file, scale_factor)
    with open(output_file, 'r') as f:
        content = f.read()
    print(content)
    os.remove(input_file)
    os.remove(output_file)