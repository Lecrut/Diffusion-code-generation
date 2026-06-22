import os
import sys
import argparse
import csv

def convert_celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9.0 / 5.0) + 32.0

def read_temperature_data(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' does not exist.")
    data_rows = []
    with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        if not reader.fieldnames:
            raise ValueError("Input CSV file is empty or missing headers.")
        if 'celsius' not in reader.fieldnames:
            raise ValueError("Input CSV must contain a 'celsius' column.")
        for row_num, row in enumerate(reader, start=2):
            raw_value = row['celsius'].strip()
            try:
                temp_c = float(raw_value)
                data_rows.append(temp_c)
            except ValueError:
                raise ValueError(f"Invalid temperature value '{raw_value}' at row {row_num}.")
    return data_rows

def process_and_output_temperatures(input_path):
    celsius_values = read_temperature_data(input_path)
    converted_data = []
    for c_val in celsius_values:
        f_val = convert_celsius_to_fahrenheit(c_val)
        converted_data.append({
            'original_celsius': c_val,
            'converted_fahrenheit': f_val
        })
    return converted_data

def main():
    parser = argparse.ArgumentParser(description='Batch convert Celsius temperatures to Fahrenheit.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file.')
    args = parser.parse_args()

    results = process_and_output_temperatures(args.input_file)
    for item in results:
        print(f"{item['original_celsius']:.2f} C -> {item['converted_fahrenheit']:.2f} F")

if __name__ == '__main__':
    test_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(test_dir, 'test_temps.csv')
    
    with open(test_file, mode='w', newline='', encoding='utf-8') as tf:
        writer = csv.writer(tf)
        writer.writerow(['celsius', 'location'])
        writer.writerow([0.0, 'Freezing'])
        writer.writerow([100.0, 'Boiling'])
        writer.writerow([36.6, 'Normal Body Temp'])

    results = process_and_output_temperatures(test_file)
    for item in results:
        print(f"{item['original_celsius']:.2f} C -> {item['converted_fahrenheit']:.2f} F")

    os.remove(test_file)

    sys.exit(0)