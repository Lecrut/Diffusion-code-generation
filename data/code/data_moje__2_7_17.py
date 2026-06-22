import csv
import tempfile
import os

def scale_volumes(input_path, output_path, factor):
    rows = []
    with open(input_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        for row in reader:
            try:
                original_volume = float(row['volume'])
                new_volume = original_volume * factor
                row['volume'] = str(new_volume)
            except ValueError:
                row['volume'] = row['volume']
            rows.append(row)
    
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    return rows

if __name__ == '__main__':
    sample_csv_content = """name,volume
Apple,100
Banana,200
Cherry,50"""
    
    temp_input = 'temp_input.csv'
    temp_output = 'temp_output.csv'
    
    with open(temp_input, 'w', encoding='utf-8') as f:
        f.write(sample_csv_content)
    
    factor = 2.5
    result = scale_volumes(temp_input, temp_output, factor)
    
    print(result)
    
    os.remove(temp_input)
    os.remove(temp_output)