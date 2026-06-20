import csv
import os
import tempfile

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def process_temperature_csv(input_file_path, output_file_path):
    try:
        if not os.path.exists(input_file_path):
            raise FileNotFoundError(f"Input file '{input_file_path}' not found.")
        
        converted_data = []
        
        with open(input_file_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            if 'temperature' not in reader.fieldnames:
                raise ValueError("CSV file must contain a 'temperature' column.")
            
            for row in reader:
                try:
                    celsius_value = float(row['temperature'])
                    fahrenheit_value = convert_celsius_to_fahrenheit(celsius_value)
                    new_row = dict(row)
                    new_row['temperature_fahrenheit'] = fahrenheit_value
                    converted_data.append(new_row)
                except ValueError:
                    raise ValueError(f"Invalid temperature value found: {row['temperature']}")
        
        if converted_data:
            fieldnames = list(converted_data[0].keys())
            with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(converted_data)
        else:
            with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
                outfile.write("")
        
        return converted_data

    except FileNotFoundError as e:
        print(f"File Error: {e}")
        return []
    except ValueError as e:
        print(f"Value Error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == '__main__':
    sample_input_content = "timestamp,temperature\n2023-10-01 08:00,20\n2023-10-01 09:00,22\n2023-10-01 10:00,25"
    
    temp_input_path = "temp_input.csv"
    temp_output_path = "temp_output.csv"
    
    try:
        with open(temp_input_path, 'w', newline='', encoding='utf-8') as f:
            f.write(sample_input_content)
            
        result = process_temperature_csv(temp_input_path, temp_output_path)
        
        if result:
            print(f"Conversion complete. Sample output row: {result[0]}")
            
            with open(temp_output_path, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(f"Row: {row}")
    finally:
        if os.path.exists(temp_input_path):
            os.remove(temp_input_path)
        if os.path.exists(temp_output_path):
            os.remove(temp_output_path)