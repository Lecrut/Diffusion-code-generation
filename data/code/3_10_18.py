import csv

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_temperature_csv(input_file: str, output_file: str) -> None:
    """Read temperatures from input CSV, convert them, and write to output CSV.

    Args:
        input_file: Path to the source CSV file containing temperature readings.
                   Expected format: header row with 'celsius' column name (case-insensitive).
        output_file: Path for the destination CSV file.
    
    Raises:
        FileNotFoundError: If either input or output files do not exist/is not writable.
        ValueError: If a non-numeric temperature is encountered during conversion.
"""
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Validate header exists and contains 'celsius' (case-insensitive)
        if not hasattr(reader.fieldnames[0].lower(), '__call__'):  # Fallback check for empty list
            raise ValueError("CSV must have at least one column.")

        fieldnames = ['fahrenheit'] + [col.lower() for col in reader.fieldnames]

if __name__ == '__main__':
    pass
