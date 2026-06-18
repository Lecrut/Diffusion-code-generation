import csv

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_temperature_file(input_path: str, output_path: str) -> None:
    """Read temperatures from input CSV, convert them, and write to output CSV.

    Args:
        input_path: Path to the source CSV file containing temperature data.
        output_path: Path to the destination CSV file for converted results.

    Raises:
        FileNotFoundError: If either input or output files do not exist (handled gracefully in main).
        ValueError: If a row contains an invalid numeric value for Celsius.
    """
    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Ensure the file has headers and 'temperature' column exists
            if reader.fieldnames is None or 'temperature' not in reader.fieldnames:
                raise ValueError("Input CSV must have a header row with a 'temperature' field.")

            rows_to_write = []
            for idx, row in enumerate(reader):
                try:
                    celsius_value = float(row['temperature'])
                    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
                    
                    # Prepare output row (preserve original headers or standardize if needed)
                    new_row = dict(row)  # Copy existing fields
                    new_row['fahrenheit'] = round(fahrenheit_value, 2)
                    rows_to_write.append(new_row)

                except ValueError:
                    raise ValueError(
                        f"Invalid temperature value at row {idx + 1}: '{row.get('temperature', '')}'. "
                        f"Expected a valid number."
                    )

        # Write results to output file with explicit headers including the new column
        fieldnames = ['original_temperature_celsius'] if 'temperature' in reader.fieldnames else list(reader.fieldnames) + ['fahrenheit']
        
        try:
            with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in rows_to_write:
                    # Ensure all keys match the defined fieldnames exactly
                    clean_row = {k: v if k in new_row else 0.0 for k, v in zip(fieldnames, [new_row.get(k, None) or 0] * len(fieldnames))} 
                    writer.writerow(clean_row)

        except PermissionError as e:
            raise IOError(f"Failed to write to output file '{output_path}': {e}") from e
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: '{input_path}'")

if __name__ == '__main__':
    # Hard-coded sample data since no user input or command-line arguments are allowed.
    # These files do not exist on the filesystem, so they will be created upon execution if run as a script with these paths? 
    # Wait, the task says "Do not include... pre-existing files". It implies I should simulate reading from existing data.
    # Since I cannot create files in the current directory of the user's environment reliably without permissions or specific setup,
    # and the prompt forbids `input()` or args, I will hardcode a list of values directly into memory 
    # to mimic what would be read from a CSV file, then write them to an output path.
    
    # To strictly adhere to "reads temperature readings from a specified CSV file", but also satisfy "run without... pre-existing files":
    # I will define the content that *would* be in the input file and simulate the reading process using this data structure, 
    # then write it out as if read from disk. This avoids dependency on actual filesystem state while fulfilling logic requirements.

    sample_csv_content = [
        ['temperature', 'location'],
        [20.5, 'New York'],
        36.1, 'London'],