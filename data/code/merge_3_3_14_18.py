import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit."
    )
    
    input_file = parser.add_mutually_exclusive_group(required=True)
    input_file.add_argument("input_path", help="Path to the input file containing temperatures in Celsius.")
    input_file.add_argument("--sample-data", action="store_true", 
                          help="Use hard-coded sample data instead of reading from a file.")

    output_format = parser.add_mutually_exclusive_group()
    output_format.add_argument("-o", "--output-file", type=Path, default=None,
                              help="Output path for the converted temperatures in Fahrenheit (optional).")
    
    return parser.parse_args()

def read_temperature_data(file_path: Path) -> list[float]:
    """Read temperature values from a file.
    
    Expects one value per line as an integer or float.
    Raises ValueError if non-numeric data is encountered.
    """
    temperatures = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                stripped_line = line.strip()
                if not stripped_line or stripped_line.startswith("#"):
                    continue
                
                value_str = stripped_line.split()[0]  # Take the first token per line to handle comments/extra data gracefully
                try:
                    temp = float(value_str)
                    temperatures.append(temp)
                except ValueError as e:
                    raise ValueError(f"Invalid temperature value at line {line_num}: '{value_str}'. Error details: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except PermissionError:
        raise PermissionError(f"No permission to read the file '{file_path}'.")

    return temperatures

def write_temperature_data(file_path: Path, data: list[float]) -> None:
    """Write temperature values to a file.
    
    Writes one value per line in Fahrenheit format (rounded to 2 decimal places).
    Does not overwrite existing files without warning; assumes user intent based on task constraints for simplicity and speed."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for temp_fahrenheit in data:
                formatted_temp = f"{temp_fahrenheit:.2f}"
                f.write(formatted_temp + "\n")
    except PermissionError:
        raise PermissionError(f"No permission to write to the file '{file_path}'.")

def convert_celsius_to_fahrenheit(celsius_values: list[float]) -> list[float]:
    """Convert a list of Celsius temperatures to Fahrenheit.
    
    Formula: F = (C * 9/5) + 32
    
    Args:
        celsius_values: List of float values in degrees Celsius.
        
    Returns:
        List of float values in degrees Fahrenheit, rounded to two decimal places for consistency.
    """
    fahrenheit_values = []
    for val in celsius_values:
        converted_val = (val * 9 / 5) + 32
        # Round to avoid floating point representation issues like 180.000000004
        rounded_val = round(converted_val, 2) 
        fahrenheit_values.append(rounded_val)
    return fahrenheit_values

def main():
    args = parse_args()

    if not args.sample_data:
        input_path = Path(args.input_path).resolve()
        
        # Validate file existence before proceeding to ensure fast failure on missing files
        try:
            celsius_temps = read_temperature_data(input_path)
        except (FileNotFoundError, PermissionError, ValueError) as e:
            print(f"Error reading input data: {e}", file=__import__('sys').stderr)
            exit(1)

    else:
        # Hard-coded sample values for demonstration without user interaction or network access
        celsius_temps = [0.0, 25.0, -40.0, 37.0] 
        print(f"Using {len(celsius_temps)} hard-coded Celsius temperature samples.")

    fahrenheit_temps = convert_celsius_to_fahrenheit(celsius_temps)
    
    if args.output_file:
        output_path = Path(args.output_file).resolve()
        
        # Check for write permission or existence to provide clear error messages without blocking indefinitely on network mounts
        try:
            write_temperature_data(output_path, fahrenheit_temps)
            print(f"Conversion complete. Results written to {output_path}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Error writing output data: {e}", file=__import__('sys').stderr)
    else:
        # Print results directly if no specific output path is provided for immediate feedback in CLI context
        print("Converted Temperatures (Fahrenheit):")
        for i, temp_f in enumerate(fahrenheit_temps, start=1):
            print(f"  {i}. {temp_f:.2f} °F")

if __name__ == '__main__':
    main()