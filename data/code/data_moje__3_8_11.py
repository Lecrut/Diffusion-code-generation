import csv
import os

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperature_file(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file {input_file} does not exist")
        
        converted_data = []
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            if not fieldnames:
                raise ValueError("Input CSV file is empty or has no headers")
            
            for row in reader:
                try:
                    temp_celsius = float(row['celsius'])
                    temp_fahrenheit = convert_celsius_to_fahrenheit(temp_celsius)
                    new_row = {**row, 'fahrenheit': temp_fahrenheit}
                    converted_data.append(new_row)
                except (ValueError, KeyError) as e:
                    raise ValueError(f"Invalid data in row: {row}. Error: {e}")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames + ['fahrenheit'])
            writer.writeheader()
            writer.writerows(converted_data)
            
        return converted_data

    except FileNotFoundError as e:
        raise e
    except IOError as e:
        raise IOError(f"An I/O error occurred: {e}")
    except ValueError as e:
        raise ValueError(f"Data processing error: {e}")

if __name__ == '__main__':
    import tempfile
    
    sample_input_name = 'sample_temps.csv'
    sample_output_name = 'output_temps.csv'
    
    sample_content = "id,celsius\n1,0\n2,25\n3,100\n4,-40\n5,37.5"
    
    with open(sample_input_name, 'w', encoding='utf-8') as f:
        f.write(sample_content)
    
    result = process_temperature_file(sample_input_name, sample_output_name)
    print(result)
    
    with open(sample_output_name, 'r', encoding='utf-8') as f:
        print(f.read())
    
    os.remove(sample_input_name)
    os.remove(sample_output_name)