import csv
import os

def convert_celsius_to_fahrenheit(input_file_path, output_file_path):
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f'Input file {input_file_path} not found.')
    results = []
    try:
        with open(input_file_path, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            headers = next(reader)
            temp_col_index = headers.index('temperature')
            for row in reader:
                try:
                    temp_c = float(row[temp_col_index])
                    temp_f = temp_c * 9 / 5 + 32
                    row.append(temp_f)
                    results.append(row)
                except ValueError:
                    continue
    except IOError:
        raise IOError(f'Error reading file {input_file_path}')
    try:
        with open(output_file_path, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(headers + ['temperature_f'])
            writer.writerows(results)
    except IOError:
        raise IOError(f'Error writing to file {output_file_path}')
    return results
if __name__ == '__main__':
    sample_input = 'sample_input.csv'
    sample_output = 'sample_output.csv'
    with open(sample_input, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'temperature'])
        writer.writerow(['1', '0'])
        writer.writerow(['2', '100'])
        writer.writerow(['3', '37'])
    results = convert_celsius_to_fahrenheit(sample_input, sample_output)
    print(results)