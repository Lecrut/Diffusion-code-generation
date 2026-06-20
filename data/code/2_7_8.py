import csv
import os

def scale_csv_volumes(input_path: str, output_path: str, scale_factor: float) -> str:
    with open(input_path, newline='', encoding='utf-8') as infile, open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            row['volume'] = float(row['volume']) * scale_factor
            writer.writerow(row)
    return output_path

if __name__ == '__main__':
    input_file = 'items_input.csv'
    output_file = 'items_output.csv'

    sample_items = [
        {'name': 'Apple', 'volume': '10.5'},
        {'name': 'Banana', 'volume': '20.0'},
        {'name': 'Cherry', 'volume': '5.25'}
    ]

    with open(input_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'volume'])
        writer.writeheader()
        writer.writerows(sample_items)

    result_path = scale_csv_volumes(input_file, output_file, 2.0)

    with open(result_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        print(rows)

    os.remove(input_file)
    os.remove(output_file)