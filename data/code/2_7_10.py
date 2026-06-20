import csv
import os
import tempfile

def scale_volumes(input_path, output_path, scale_factor):
    with open(input_path, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        scaled_rows = []
        for row in reader:
            new_row = dict(row)
            volume = float(new_row.get('volume', 0))
            new_row['volume'] = volume * scale_factor
            scaled_rows.append(new_row)

    with open(output_path, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scaled_rows)

    return scaled_rows

if __name__ == '__main__':
    input_csv = tempfile.mktemp(suffix='.csv')
    output_csv = tempfile.mktemp(suffix='.csv')

    with open(input_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['item', 'volume'])
        writer.writerow(['apple', '10'])
        writer.writerow(['banana', '20'])
        writer.writerow(['cherry', '15'])

    scale_factor = 2.5
    result = scale_volumes(input_csv, output_csv, scale_factor)
    print(result)

    with open(output_csv, 'r') as f:
        content = f.read()
    print(content)

    os.remove(input_csv)
    os.remove(output_csv)