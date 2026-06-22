import csv
import os
import tempfile

def process_item_volumes(input_csv_path, output_csv_path, scale_factor):
    scaled_rows = []
    with open(input_csv_path, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            item_name = row['item_name']
            volume = float(row['volume'])
            scaled_volume = volume * scale_factor
            scaled_rows.append({'item_name': item_name, 'volume': scaled_volume})

    with open(output_csv_path, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['item_name', 'volume'])
        writer.writeheader()
        writer.writerows(scaled_rows)

    return scaled_rows

if __name__ == '__main__':
    input_csv_content = "item_name,volume\nApple,10\nBanana,20\nOrange,30\n"
    scale_factor = 2.5

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_input:
        tmp_input.write(input_csv_content)
        input_path = tmp_input.name

    output_path = tempfile.mktemp(suffix='.csv')

    try:
        result = process_item_volumes(input_path, output_path, scale_factor)
        print(result)
    finally:
        os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)