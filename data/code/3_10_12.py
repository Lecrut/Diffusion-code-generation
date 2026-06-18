import csv

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_temperature_csv(input_file: str, output_file: str) -> None:
    """Read temperatures from input CSV, convert to Fahrenheit, and write to output CSV.

    Args:
        input_file (str): Path to the source CSV file containing temperature readings.
                          Expected format: a single column with numeric values in Celsius.
        output_file (str): Path where the converted data will be written.
    """
    try:
        # Read from input file
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)

            rows_to_write = []

            for row in reader:
                if not row or all(cell.strip() == '' for cell in row):
                    continue  # Skip empty lines

                try:
                    celsius_value = float(row[0])
                    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
                    rows_to_write.append([fahrenheit_value])
                except ValueError as e:
                    raise ValueError(f"Invalid temperature value found in input file at current row: {e}")

        # Write to output file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for row in rows_to_write:
                writer.writerow(row)

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_file}' not found.")
    except PermissionError:
        raise PermissionError("Permission denied to read from input or write to output file.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or pre-existing files.
    # Simulating a temporary CSV content with known Celsius readings.
    sample_celsius_data = [20, 35, -10, 98.6]

    input_filename = 'sample_temps.csv'
    output_filename = 'converted_temps.csv'

    try:
        process_temperature_csv(input_filename, output_filename)
        print(f"Conversion complete. Output written to {output_filename}")
    except FileNotFoundError as e:
        # Since we are simulating data in memory but writing to files that don't exist yet,
        # this block handles the case where the script tries to read from a non-existent file.
        raise RuntimeError("Simulation note: The input file does not exist on disk because "
                         f"this is a self-contained test run using hardcoded logic.") from e