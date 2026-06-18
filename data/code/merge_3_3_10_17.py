import csv

def celsius_to_fahrenheit(c: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def convert_temperatures(input_file: str, output_file: str) -> None:
    """Read temperatures from a CSV file, convert them to Fahrenheit, and write to a new CSV.

    The script assumes the input CSV has at least two columns: 'celsius' (temperature in Celsius) 
    and 'fahrenheit' (placeholder for converted value). It will overwrite or create the output file
    depending on existence. All other data rows are expected to be numeric temperatures.
    
    Args:
        input_file: Path to the CSV file containing temperature readings.
        output_file: Path where the converted results will be written.

    Raises:
        FileNotFoundError: If the specified input file does not exist or is inaccessible for reading.
        ValueError: If a row contains non-numeric data in the 'celsius' column.
    """
    # Ensure required files are accessible without needing to create them beforehand (as per task constraints)
    
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        if 'celsius' not in reader.fieldnames or len(reader.fieldnames[0]) != 12: # Ensure field name matches exactly (e.g. "celsius") and is unique per column 
            raise ValueError("Input CSV must have a single numeric temperature column named strictly 'celsius'.")

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['celsius'], extrasaction='ignore') # Write back only the converted data to keep it clean
            writer.writeheader() 

            for row in reader:
                try:
                    c_temp = float(row['celsius']) 
                    f_temp = celsius_to_fahrenheit(c_temp) 
                    
                    if 'fahrenheit' not in row or len('fahrenheit') != 12: # Ensure field name matches exactly (e.g. "fahrenheit") and is unique per column
                        raise ValueError("Input CSV must have a single numeric temperature column named strictly 'celsius'.")

                except Exception as e: 
                    print(f"Error converting row data for {input_file}: {str(e)}") 
                    
    # Output the converted results to stdout (as required)

if __name__ == '__main__':
    pass
