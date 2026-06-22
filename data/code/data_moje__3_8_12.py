import csv
import os

def celsius_to_fahrenheit(celsius):
    return float(celsius) * 9.0 / 5.0 + 32.0

def convert_temperature_csv(input_path, output_path, temp_column=0):
    try:
        with open(input_path, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            rows = list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_path}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied reading '{input_path}'.")
    except Exception as e:
        raise IOError(f"Error reading '{input_path}': {e}")

    if not rows:
        raise ValueError("Input CSV file is empty.")

    header = rows[0]
    if temp_column >= len(header):
        raise IndexError(
            f"Column index {temp_column} is out of range for header with {len(header)} columns."
        )

    try:
        with open(output_path, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            for row in rows[1:]:
                if not row:
                    writer.writerow(row)
                    continue
                if temp_column >= len(row):
                    raise IndexError(
                        f"Row has fewer columns than expected: {len(row)} < {temp_column + 1}"
                    )
                try:
                    celsius_val = float(row[temp_column])
                    fahrenheit_val = celsius_to_fahrenheit(celsius_val)
                    new_row = list(row)
                    new_row[temp_column] = str(fahrenheit_val)
                    writer.writerow(new_row)
                except ValueError:
                    raise ValueError(
                        f"Cannot convert value '{row[temp_column]}' at column {temp_column} to float."
                    )
    except PermissionError:
        raise PermissionError(f"Permission denied writing to '{output_path}'.")
    except Exception as e:
        raise IOError(f"Error writing '{output_path}': {e}")

    return output_path

if __name__ == '__main__':
    input_file = 'input_temps.csv'
    output_file = 'output_temps.csv'

    with open(input_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['location', 'temperature_c'])
        writer.writerow(['New York', '25.0'])
        writer.writerow(['London', '15.5'])
        writer.writerow(['Tokyo', '30.0'])

    result_path = convert_temperature_csv(input_file, output_file, temp_column=1)

    with open(result_path, mode='r', newline='') as f:
        reader = csv.reader(f)
        converted_data = list(reader)

    print(converted_data)

    os.remove(input_file)
    os.remove(output_file)