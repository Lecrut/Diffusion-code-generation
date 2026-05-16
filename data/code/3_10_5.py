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
                try:
                    celsius = float(row[0])
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    output_data.append([row[0], row[1], f"{fahrenheit:.2f}"])
                except ValueError:
                    print(f"Skipping row due to invalid temperature value: {row}")
                except IndexError:
                    print(f"Skipping row due to insufficient columns: {row}")
        with open(output_filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(output_data)
        print(f"Successfully processed data. Results written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    INPUT_FILE = 'input_temps.csv'
    OUTPUT_FILE = 'output_temps.csv'
    sample_data = [
        ["Temperature_C", "Location"],
        ["20.0", "Room A"],
        ["25.5", "Room B"],
        ["30.1", "Room C"],
        ["invalid", "Room D"]
    ]
    try:
        with open(INPUT_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sample_data)
        process_temperature_data(INPUT_FILE, OUTPUT_FILE)
    except Exception as e:
        print(f"Setup error: {e}")