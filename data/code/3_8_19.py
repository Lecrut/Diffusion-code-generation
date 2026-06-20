import csv
import os
import tempfile

def convert_temperatures(input_file, output_file):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            if not fieldnames:
                raise ValueError("CSV file is empty or has no header.")
            
            temperature_column = None
            for col in fieldnames:
                if 'temp' in col.lower() or 'celsius' in col.lower():
                    temperature_column = col
                    break
            
            if not temperature_column:
                raise ValueError("No temperature column found in the CSV.")

            rows_data = []
            for row in reader:
                try:
                    celsius = float(row[temperature_column])
                    fahrenheit = (celsius * 9/5) + 32
                    row['fahrenheit'] = f"{fahrenheit:.2f}"
                    rows_data.append(row)
                except ValueError:
                    continue

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames + ['fahrenheit'])
            writer.writeheader()
            writer.writerows(rows_data)
        
        return rows_data

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    temp_dir = tempfile.gettempdir()
    sample_input_path = os.path.join(temp_dir, 'sample_temp_input.csv')
    sample_output_path = os.path.join(temp_dir, 'sample_temp_output.csv')

    with open(sample_input_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'location', 'temperature_celsius'])
        writer.writerow([1, 'London', 20.0])
        writer.writerow([2, 'Paris', 25.5])
        writer.writerow([3, 'Berlin', -5.0])

    result = convert_temperatures(sample_input_path, sample_output_path)
    print(result)
    
    with open(sample_output_path, 'r', newline='', encoding='utf-8') as f:
        content = f.read()
        print(content)

    os.remove(sample_input_path)
    os.remove(sample_output_path)