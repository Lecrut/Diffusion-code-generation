import csv
import os
import tempfile

def convert_csv_celsius_to_fahrenheit(input_path, output_path):
    with open(input_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        rows = list(reader)

    converted_rows = []
    for row in rows:
        converted_row = []
        for value in row:
            try:
                celsius = float(value)
                fahrenheit = (celsius * 9 / 5) + 32
                converted_row.append(f"{fahrenheit:.2f}")
            except ValueError:
                converted_row.append(value)
        converted_rows.append(converted_row)

    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(converted_rows)

    return converted_rows

def main():
    temp_data = [[
        "Temperature", "Notes"
    ], [
        "0", "Freezing"
    ], [
        "100", "Boiling"
    ]]

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_in:
        writer = csv.writer(tmp_in)
        writer.writerows(temp_data)
        tmp_in_path = tmp_in.name

    tmp_out_path = tmp_in_path + ".out"

    try:
        result = convert_csv_celsius_to_fahrenheit(tmp_in_path, tmp_out_path)
        for row in result:
            print(row)
    finally:
        if os.path.exists(tmp_in_path):
            os.remove(tmp_in_path)
        if os.path.exists(tmp_out_path):
            os.remove(tmp_out_path)

if __name__ == '__main__':
    main()