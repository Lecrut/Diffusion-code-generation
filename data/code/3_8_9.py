import csv
import os
import tempfile

def convert_celsius_to_fahrenheit(input_path: str, output_path: str) -> dict:
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f'Input file not found: {input_path}')
    results = {}
    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            if fieldnames is None:
                raise ValueError('Input CSV file is empty or has no headers.')
            temp_col = None
            for col in fieldnames:
                if 'celsius' in col.lower() or (col.lower() == 'temp' and 'fahrenheit' not in [f.lower() for f in fieldnames]):
                    temp_col = col
                    break
            if temp_col is None:
                raise ValueError('Could not identify a Celsius temperature column in the CSV.')
            new_fieldnames = [f'{col}_fahrenheit' if col == temp_col else col for col in fieldnames]
            fd, temp_out = tempfile.mkstemp(suffix='.csv', prefix='temp_convert_')
            try:
                with open(fd, mode='w', newline='', encoding='utf-8') as tempfile_obj:
                    writer = csv.DictWriter(tempfile_obj, fieldnames=new_fieldnames)
                    writer.writeheader()
                    records_processed = 0
                    for row in reader:
                        try:
                            celsius_val = float(row[temp_col])
                        except ValueError:
                            raise ValueError(f"Invalid temperature value '{row[temp_col]}' in row {records_processed + 1}.")
                        fahrenheit_val = celsius_val * 9 / 5 + 32
                        new_row = {}
                        for field in new_fieldnames:
                            if field == f'{temp_col}_fahrenheit':
                                new_row[field] = f'{fahrenheit_val:.2f}'
                            else:
                                new_row[field] = row.get(field, '')
                        writer.writerow(new_row)
                        records_processed += 1
                with open(temp_out, mode='r', newline='', encoding='utf-8') as f_in:
                    content = f_in.read()
                with open(output_path, mode='w', newline='', encoding='utf-8') as f_out:
                    f_out.write(content)
                os.close(fd)
                os.unlink(temp_out)
                results[os.path.basename(input_path)] = records_processed
            except Exception as e:
                os.close(fd)
                if os.path.exists(temp_out):
                    os.unlink(temp_out)
                raise IOError(f'Error writing output file: {e}')
    except FileNotFoundError:
        raise
    except ValueError as e:
        raise
    except IOError as e:
        raise
    return results
if __name__ == '__main__':
    input_csv_content = 'location,celsius,timestamp\nNew York,0,2023-10-01\nLondon,10,2023-10-01\nTokyo,20,2023-10-01'
    input_filename = 'input_temps.csv'
    output_filename = 'output_temps.csv'
    with open(input_filename, mode='w', newline='', encoding='utf-8') as f:
        f.write(input_csv_content)
    try:
        result = convert_celsius_to_fahrenheit(input_filename, output_filename)
        print(result)
    finally:
        for filename in [input_filename, output_filename]:
            if os.path.exists(filename):
                os.unlink(filename)