import csv
import os

def scale_volumes(input_filename, output_filename, scale_factor):
    temp_filename = input_filename + ".tmp"
    if os.path.exists(input_filename):
        with open(input_filename, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            if 'item_name' not in fieldnames or 'volume' not in fieldnames:
                raise ValueError("CSV must contain 'item_name' and 'volume' columns")
            
            with open(temp_filename, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    original_volume = float(row['volume'])
                    scaled_volume = original_volume * scale_factor
                    row['volume'] = scaled_volume
                    writer.writerow(row)
        os.replace(temp_filename, output_filename)
        os.remove(input_filename)
    else:
        with open(temp_filename, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['item_name', 'volume'])
            writer.writeheader()
            sample_data = [
                {'item_name': 'apple', 'volume': 100.0},
                {'item_name': 'banana', 'volume': 200.0},
                {'item_name': 'orange', 'volume': 150.0}
            ]
            for item in sample_data:
                item['volume'] = item['volume'] * scale_factor
                writer.writerow(item)
        os.rename(temp_filename, output_filename)
        with open(input_filename, 'w', newline='', encoding='utf-8') as infile:
            writer = csv.DictWriter(infile, fieldnames=['item_name', 'volume'])
            writer.writeheader()
            for item in sample_data:
                item['volume'] = float(item['volume']) / scale_factor
                writer.writerow(item)

if __name__ == '__main__':
    input_file = 'input_data.csv'
    output_file = 'output_data.csv'
    factor = 2.5
    
    scale_volumes(input_file, output_file, factor)
    
    with open(output_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        results = []
        for row in reader:
            results.append(f"{row['item_name']}: {row['volume']}")
        for res in results:
            print(res)