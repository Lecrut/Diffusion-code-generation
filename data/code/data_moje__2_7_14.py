import csv
import tempfile
import os

def scale_volumes(input_file, output_file, scale_factor):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in rows:
        if 'volume' in row and row['volume']:
            try:
                original_volume = float(row['volume'])
                scaled_volume = original_volume * scale_factor
                row['volume'] = str(scaled_volume)
            except ValueError:
                continue

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return f"Processed {len(rows)} items with scale factor {scale_factor}"

if __name__ == '__main__':
    sample_csv_content = """name,volume
apple,10.5
banana,20.0
orange,15.75"""
    
    temp_input = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8')
    temp_input.write(sample_csv_content)
    temp_input.close()
    
    temp_output = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='_scaled.csv', encoding='utf-8')
    temp_output_name = temp_output.name
    temp_output.close()

    result = scale_volumes(temp_input.name, temp_output_name, 2.0)
    print(result)

    with open(temp_output_name, 'r', encoding='utf-8') as f:
        output_content = f.read()
    print(output_content)

    os.unlink(temp_input.name)
    os.unlink(temp_output_name)