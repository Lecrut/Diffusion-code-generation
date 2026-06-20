import csv
import os
import sys

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def process_temperature_csv(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader, None)
            
            if header is None:
                raise ValueError("Input file is empty.")
            
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)
                
                for row in reader:
                    try:
                        if len(row) < 1:
                            continue
                        celsius_value = float(row[0])
                        fahrenheit_value = convert_celsius_to_fahrenheit(celsius_value)
                        writer.writerow([fahrenheit_value])
                    except ValueError:
                        continue
        return True
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == '__main__':
    sample_data_path = "temp_readings.csv"
    output_data_path = "temp_readings_fahrenheit.csv"
    
    with open(sample_data_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Temperature_C"])
        writer.writerow(["0"])
        writer.writerow(["100"])
        writer.writerow(["-40"])
        writer.writerow(["37.5"])
    
    success = process_temperature_csv(sample_data_path, output_data_path)
    
    if success:
        with open(output_data_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    
    os.remove(sample_data_path)
    os.remove(output_data_path)