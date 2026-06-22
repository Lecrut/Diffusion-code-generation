import csv
import os
import tempfile

def scale_volumes(input_path, output_path, factor):
    temp_path = output_path + '.tmp'
    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            if fieldnames is None:
                fieldnames = ['name', 'volume']
            
            with open(temp_path, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    try:
                        original_volume = float(row['volume'])
                    except (ValueError, KeyError):
                        original_volume = 0.0
                    scaled_volume = original_volume * factor
                    row['volume'] = scaled_volume
                    writer.writerow(row)
        os.replace(temp_path, output_path)
        return f"Processed {output_path} with factor {factor}"
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise e

if __name__ == '__main__':
    sample_csv_content = "name,volume\napple,10\nbanana,20\norange,30"
    test_input_path = 'test_input.csv'
    test_output_path = 'test_output.csv'
    test_factor = 2.5
    
    with open(test_input_path, 'w', newline='', encoding='utf-8') as f:
        f.write(sample_csv_content)
    
    result = scale_volumes(test_input_path, test_output_path, test_factor)
    print(result)
    
    with open(test_output_path, 'r', encoding='utf-8') as f:
        print(f.read())
    
    os.remove(test_input_path)
    os.remove(test_output_path)