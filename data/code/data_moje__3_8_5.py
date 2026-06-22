import csv
import os

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def process_temperature_csv(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as infile:
            reader = csv.DictReader(infile)
            if not reader.fieldnames:
                raise ValueError("Input file is empty or has no header.")
            
            fieldnames = list(reader.fieldnames)
            if 'Celsius' not in fieldnames:
                raise ValueError("Input file must contain a 'Celsius' column.")
            
            output_fieldnames = [f for f in fieldnames if f != 'Celsius']
            output_fieldnames.append('Fahrenheit')
            
            rows = []
            for row in reader:
                try:
                    celsius_val = float(row['Celsius'])
                    row['Fahrenheit'] = convert_celsius_to_fahrenheit(celsius_val)
                    rows.append({k: row[k] for k in output_fieldnames if k in row})
                except ValueError:
                    raise ValueError(f"Invalid temperature value in row: {row}")
        
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=output_fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        return output_file, f"Successfully converted {len(rows)} readings."
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_file}' not found.")
    except IOError as e:
        raise IOError(f"Error accessing file: {e}")

if __name__ == '__main__':
    sample_data = """Name,Celsius
Alice,20
Bob,30
Charlie,-5
"""
    input_filename = 'temp_input.csv'
    output_filename = 'temp_output.csv'
    
    with open(input_filename, 'w') as f:
        f.write(sample_data)
    
    try:
        result_file, result_message = process_temperature_csv(input_filename, output_filename)
        with open(result_file, 'r') as f:
            content = f.read()
        print(result_message)
        print(content)
    except Exception as e:
        print(f"Error: {e}")
    
    if os.path.exists(input_filename):
        os.remove(input_filename)
    if os.path.exists(output_filename):
        os.remove(output_filename)