import csv
import os
import tempfile

def scale_volumes(input_file, output_file, scale_factor):
    rows = []
    with open(input_file, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        volume_index = header.index('volume')
        rows.append(header)
        for row in reader:
            new_row = row.copy()
            new_row[volume_index] = float(row[volume_index]) * scale_factor
            rows.append(new_row)

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    return output_file

def create_sample_csv(file_path, data):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    sample_data = [
        ['item', 'volume'],
        ['apple', '1.0'],
        ['banana', '2.5'],
        ['cherry', '0.5']
    ]

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, 'input.csv')
        output_path = os.path.join(tmpdir, 'output.csv')

        create_sample_csv(input_path, sample_data)

        scale_factor = 3.0
        result_file = scale_volumes(input_path, output_path, scale_factor)

        with open(result_file, 'r') as f:
            print(f.read().strip())