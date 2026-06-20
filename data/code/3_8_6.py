import csv
import os
import tempfile

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def process_temperature_csv(input_file, output_file):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            
            if 'temperature_celsius' not in fieldnames:
                raise ValueError("Input CSV must contain a column named 'temperature_celsius'")
                
            if 'temperature_fahrenheit' in fieldnames:
                raise ValueError("Output column name 'temperature_fahrenheit' already exists in input columns")
            
            output_fieldnames = list(fieldnames) + ['temperature_fahrenheit']
            
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=output_fieldnames)
                writer.writeheader()
                
                for row in reader:
                    try:
                        celsius_val = float(row['temperature_celsius'])
                        fahrenheit_val = convert_celsius_to_fahrenheit(celsius_val)
                        row['temperature_fahrenheit'] = fahrenheit_val
                        writer.writerow(row)
                    except ValueError:
                        row['temperature_fahrenheit'] = 'Invalid Data'
                        writer.writerow(row)
        return output_file
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_file} was not found")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

if __name__ == '__main__':
    input_filename = 'input_temps.csv'
    output_filename = 'output_temps.csv'
    
    sample_data = [
        ['temperature_celsius', 'location'],
        ['0', 'North Pole'],
        ['25', 'Desert'],
        ['-40', 'Antarctica'],
        ['100', 'Boiling Water']
    ]
    
    with open(input_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
    
    result_file = process_temperature_csv(input_filename, output_filename)
    
    with open(result_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        results = list(reader)
    
    print(results)