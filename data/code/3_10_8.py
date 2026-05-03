import csv
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def process_temperatures(input_filename, output_filename):
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
                    if len(row) > 0:
                        try:
                            celsius = float(row[0].strip())
                            fahrenheit = celsius_to_fahrenheit(celsius)
                            writer.writerow([f"{fahrenheit:.2f}"])
                        except ValueError:
                            pass
                    else:
                        writer.writerow([])
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except IOError as e:
        print(f"Error during file I/O: {e}")
if __name__ == '__main__':
    INPUT_FILE = 'input_temps.csv'
    OUTPUT_FILE = 'output_temps.csv'
    sample_data = [
        ['Temperature_C', 'Location'],
        ['20.0', 'Room A'],
        ['25.5', 'Room B'],
        ['30.1', 'Room C'],
        ['15.0', 'Room D']
    ]
    try:
        with open(INPUT_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sample_data)
        process_temperatures(INPUT_FILE, OUTPUT_FILE)
    except IOError as e:
        print(f"An error occurred while setting up the sample input file: {e}")