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
            output_data = [header + ["Fahrenheit"]]
            for row in reader:
                if len(row) > 0:
                    try:
                        celsius = float(row[0].strip())
                        fahrenheit = celsius_to_fahrenheit(celsius)
                        output_data.append([row[0].strip(), row[1].strip(), f"{fahrenheit:.2f}"])
                    except ValueError:
                        print(f"Skipping invalid temperature reading: {row}")
                else:
                    output_data.append(["", "Error", "No data"])
        with open(output_filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(output_data)
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    input_file = 'input_temps.csv'
    output_file = 'output_temps.csv'
    sample_data = [
        ['Temperature_C', 'Location'],
        ['20.0', 'New York'],
        ['37.5', 'London'],
        ['15.0', 'Tokyo'],
        ['25.0', 'Paris']
    ]
    try:
        with open(input_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sample_data)
        process_temperature_data(input_file, output_file)
    except Exception as e:
        print(f"Setup error: {e}")