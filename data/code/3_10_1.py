import csv
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def process_temperature_data(input_filename, output_filename):
    try:
        with open(input_filename, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader, None)
            if header is None:
                return
            with open(output_filename, mode='w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)
                for row in reader:
                    try:
                        celsius = float(row[0])
                        fahrenheit = celsius_to_fahrenheit(celsius)
                        writer.writerow([fahrenheit])
                    except ValueError:
                        print(f"Skipping row due to invalid temperature value: {row}")
                    except IndexError:
                        print(f"Skipping row due to insufficient data: {row}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
if __name__ == '__main__':
    input_file = 'input_temps.csv'
    output_file = 'output_temps.csv'
    sample_data = [
        ['Temperature_C'],
        ['20.0'],
        ['25.5'],
        ['30.1'],
        ['15.0']
    ]
    try:
        with open(input_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sample_data)
        process_temperature_data(input_file, output_file)
    except IOError as e:
        print(f"Error writing sample input file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")