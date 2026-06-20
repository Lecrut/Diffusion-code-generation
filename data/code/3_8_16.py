import csv
import os
import tempfile

def convert_csv_temperatures(input_file, output_file):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            if 'celsius' not in reader.fieldnames:
                raise ValueError("Input CSV must contain a 'celsius' column.")
            
            fieldnames = reader.fieldnames
            fieldnames.remove('celsius')
            fieldnames.append('fahrenheit')
            
            rows = []
            for row in reader:
                celsius = float(row['celsius'])
                fahrenheit = (celsius * 9/5) + 32
                row['fahrenheit'] = f"{fahrenheit:.2f}"
                rows.append(row)
                
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            
        return f"Conversion successful. Output written to {output_file}"
    except FileNotFoundError:
        return f"Error: The file {input_file} was not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    sample_input_path = "temp_input.csv"
    sample_output_path = "temp_output.csv"
    
    with open(sample_input_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'celsius', 'location'])
        writer.writeheader()
        writer.writerow({'id': '1', 'celsius': '0', 'location': 'Arctic'})
        writer.writerow({'id': '2', 'celsius': '100', 'location': 'Desert'})
        writer.writerow({'id': '3', 'celsius': '-40', 'location': 'Antarctica'})
        
    result = convert_csv_temperatures(sample_input_path, sample_output_path)
    print(result)
    
    with open(sample_output_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    
    os.remove(sample_input_path)
    os.remove(sample_output_path)