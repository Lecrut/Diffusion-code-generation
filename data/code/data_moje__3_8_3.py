import csv
import os

def convert_temperatures(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            
            if 'celsius' not in [f.lower() for f in fieldnames]:
                raise ValueError("Input CSV must contain a column named 'celsius'.")
            
            celsius_col = next(f for f in fieldnames if f.lower() == 'celsius')
            
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for row in reader:
                    try:
                        celsius = float(row[celsius_col])
                        row['fahrenheit'] = (celsius * 9/5) + 32
                        writer.writerow(row)
                    except ValueError:
                        row['fahrenheit'] = "Invalid"
                        writer.writerow(row)
        return output_file
    except FileNotFoundError as e:
        return str(e)
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    sample_input = "sample_temps.csv"
    sample_output = "converted_temps.csv"
    
    with open(sample_input, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "celsius", "location"])
        writer.writerow(["1", "0", "North"])
        writer.writerow(["2", "100", "South"])
        writer.writerow(["3", "37", "East"])
    
    result = convert_temperatures(sample_input, sample_output)
    print(result)
    
    with open(sample_output, 'r', newline='', encoding='utf-8') as f:
        print(f.read())
    
    os.remove(sample_input)
    os.remove(sample_output)