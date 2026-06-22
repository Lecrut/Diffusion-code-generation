import csv
import os

def convert_celsius_to_fahrenheit(input_filename, output_filename):
    results = []
    try:
        with open(input_filename, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if not row:
                    continue
                celsius_str = row[0]
                celsius_val = float(celsius_str)
                fahrenheit_val = (celsius_val * 9/5) + 32
                results.append([fahrenheit_val])
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file {input_filename} not found.")
    except ValueError:
        raise ValueError("Invalid temperature data in input file.")
    except Exception as e:
        raise e

    with open(output_filename, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(results)
    
    return results

if __name__ == '__main__':
    input_file = 'input_temps.csv'
    output_file = 'output_temps.csv'
    
    sample_data = [
        ['0'],
        ['100'],
        ['-40']
    ]
    
    with open(input_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
        
    converted_values = convert_celsius_to_fahrenheit(input_file, output_file)
    
    for val in converted_values:
        print(val[0])
    
    os.remove(input_file)
    os.remove(output_file)