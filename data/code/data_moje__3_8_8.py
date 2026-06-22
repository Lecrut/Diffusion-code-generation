import csv
import os

def read_temperatures(input_path):
    rows = []
    with open(input_path, newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        temp_index = header.index('Temperature')
        for row in reader:
            celsius = float(row[temp_index])
            rows.append(celsius)
    return rows

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def write_temperatures(output_path, fahrenheit_values):
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Temperature_Celsius', 'Temperature_Fahrenheit'])
        for f in fahrenheit_values:
            writer.writerow([f, f])

def process_temperatures(input_path, output_path):
    try:
        celsius_values = read_temperatures(input_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file {input_path} not found.")
    except StopIteration:
        raise ValueError("Input file is empty or missing header.")
    except Exception as e:
        raise RuntimeError(f"Error reading input file: {e}")

    fahrenheit_values = [celsius_to_fahrenheit(c) for c in celsius_values]

    try:
        write_temperatures(output_path, fahrenheit_values)
    except Exception as e:
        raise RuntimeError(f"Error writing output file: {e}")

    return fahrenheit_values

def create_sample_input(path, values):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Temperature', 'Sensor_ID'])
        for i, val in enumerate(values):
            writer.writerow([val, i])

if __name__ == '__main__':
    input_file = 'sample_input.csv'
    output_file = 'sample_output.csv'

    sample_temps = [0.0, 100.0, 36.6, -40.0]
    create_sample_input(input_file, sample_temps)

    result = process_temperatures(input_file, output_file)
    print(result)