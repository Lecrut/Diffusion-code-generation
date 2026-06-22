import argparse
import csv
import os

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def batch_convert_celsius_to_fahrenheit(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    results = []
    with open(input_path, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        if 'celsius' not in reader.fieldnames:
            raise ValueError("Input CSV must contain a 'celsius' column.")
        
        for row in reader:
            try:
                temp_c = float(row['celsius'])
                temp_f = celsius_to_fahrenheit(temp_c)
                results.append({
                    'celsius': temp_c,
                    'fahrenheit': temp_f
                })
            except ValueError:
                raise ValueError(f"Invalid temperature value in row: {row}")

    with open(output_path, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['celsius', 'fahrenheit'])
        writer.writeheader()
        for row in results:
            writer.writerow(row)
            
    return results

if __name__ == '__main__':
    sample_data = "celsius\n100\n0\n37\n-40\n"
    sample_input_file = "input_temp.csv"
    sample_output_file = "output_temp.csv"
    
    with open(sample_input_file, 'w', newline='') as f:
        f.write(sample_data)
    
    result = batch_convert_celsius_to_fahrenheit(sample_input_file, sample_output_file)
    
    for item in result:
        print(item)