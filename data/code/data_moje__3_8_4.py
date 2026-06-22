import csv
import tempfile
import os

def convert_csv_to_fahrenheit(input_path, output_path):
    with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise ValueError("Input file is empty or has no headers.")
        with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                converted_row = {}
                for key, value in row.items():
                    try:
                        temp_c = float(value)
                        temp_f = (temp_c * 9 / 5) + 32
                        converted_row[key] = str(temp_f)
                    except ValueError:
                        converted_row[key] = value
                writer.writerow(converted_row)
    return output_path

def run_sample():
    sample_input = """TempC
0
100
-40
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f_in:
        f_in.write(sample_input)
        input_path = f_in.name

    output_path = input_path.replace('.csv', '_out.csv')
    try:
        result_path = convert_csv_to_fahrenheit(input_path, output_path)
        with open(result_path, mode='r', encoding='utf-8') as f_out:
            reader = csv.DictReader(f_out)
            rows = list(reader)
        return rows
    finally:
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)

if __name__ == '__main__':
    results = run_sample()
    for row in results:
        print(row)