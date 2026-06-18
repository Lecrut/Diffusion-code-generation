import argparse
from pathlib import Path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert temperature data from Celsius to Fahrenheit in a batch."
    )
    
    input_file = parser.add_mutually_exclusive_group(required=True)
    input_file.add_argument("--input", "-i", type=str, help="Path to the input file containing temperatures.")
    input_file.add_argument("--sample", action="store_true", help="Use hard-coded sample values instead of a file.")

    output_format = parser.add_mutually_exclusive_group(required=True)
    output_format.add_argument("--output", "-o", type=str, help="Path to the output file for converted data.")
    output_format.add_argument("--stdout", action="store_true", help="Print results directly to stdout instead of a file.")

    return parser.parse_args()

def read_temperature_data(file_path: Path) -> list[float]:
    """Read temperature values from a CSV or text file. Assumes the first column contains numeric Celsius values."""
    temperatures = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                parts = [part.strip() for part in line.split(",")]
                
                # Skip header lines if they exist (simple check)
                if len(parts) > 0 and "Celsius" in str(parts[0]):
                    continue
                
                try:
                    celsius_value = float(parts[0])
                    temperatures.append(celsius_value)
                except ValueError as e:
                    raise ValueError(f"Invalid temperature value at line {line_num}: '{parts[0]}'. Error details: {e}") from e
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file was not found: {file_path.absolute()}")
    except PermissionError:
        raise PermissionError(f"No permission to read the file: {file_path.absolute()}")

    return temperatures

def convert_celsius_to_fahrenheit(temperatures: list[float]) -> list[float]:
    """Convert a list of Celsius values to Fahrenheit."""
    fahrenheit_values = []
    
    for c in temperatures:
        # Formula: F = (C * 9/5) + 32
        f_value = round((c * 1.8) + 32, 4)
        fahrenheit_values.append(f_value)
        
    return fahrenheit_values

def write_output_data(data: list[float], output_path: Path | None):
    """Write the converted data to a file or stdout."""
    
    if not data:
        print("No temperature data was processed.")
        return

    # Determine the separator based on input assumption (comma-separated)
    separator = ","
    
    try:
        with open(output_path, "w", encoding="utf-8") as f_out:
            for val in data:
                f_out.write(f"{val}{separator}\n")
        
        print(f"Successfully wrote {len(data)} records to {output_path.absolute()}")
    except PermissionError:
        raise PermissionError(f"No permission to write to the output file: {output_path}")

def main():
    """Main execution block."""
    
    args = parse_args()

    if args.sample:
        # Hard-coded sample values for demonstration without user input or files
        temperatures = [0.0, 25.5, -10.3, 100.0]
        
        print("Using hard-coded sample data.")
    else:
        try:
            file_path = Path(args.input)
            
            if not file_path.exists():
                raise FileNotFoundError(f"The input file was not found: {file_path.absolute()}")
                
            temperatures = read_temperature_data(file_path)
            print(f"Read {len(temperatures)} temperature records from {args.input}")

        except (FileNotFoundError, PermissionError, ValueError) as e:
            print(f"Critical Error reading input data: {e}", file=__import__('sys').stderr)
            return 1
    
    try:
        fahrenheit_data = convert_celsius_to_fahrenheit(temperatures)
        
        if args.stdout:
            for val in fahrenheit_data:
                print(val)
            
            # If no output path specified, we assume stdout is the target. 
            # However, argparse mutually exclusive groups require one of them to be set.
            # The logic above handles printing directly.
        
        else:
            try:
                file_path = Path(args.output)
                
                if not args.sample and (not file_path.exists() or file_path.stat().st_size == 0):
                    print(f"Output path will overwrite existing content at {file_path.absolute()}")

                write_output_data(fahrenheit_data, file_path)
            except PermissionError as e:
                print(f"Critical Error writing output data: {e}", file=__import__('sys').stderr)
                return 1
                
    except Exception as e:
        # Catch any unexpected errors during conversion or processing
        error_msg = f"An unexpected error occurred while converting temperatures. Details: {str(e)}"
        print(error_msg, file=__import__('sys').stderr)
        return 1
        
    return 0

if __name__ == '__main__':
    exit(main())