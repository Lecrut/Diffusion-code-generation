import argparse
from pathlib import Path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit."
    )
    
    input_file = parser.add_mutually_exclusive_group(required=True)
    input_file.add_argument("-i", "--input-file", type=str, help="Path to the input file containing temperatures.")
    input_file.add_argument("--sample-data", action="store_true", help="Use hard-coded sample data instead of a file.")

    output_format = parser.add_mutually_exclusive_group(required=True)
    output_format.add_argument("-o", "--output-file", type=str, help="Path to the output file for converted temperatures.")
    output_format.add_argument("--print-only", action="store_true", help="Print results to stdout instead of writing to a file.")

    return parser.parse_args()

def read_temperature_data(file_path: Path) -> list[float]:
    """Read temperature values from a CSV or text file. Assumes the first column is numeric Celsius data."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
        
        # Skip header if present (assuming standard format)
        start_index = 0
        if len(lines) > 1 and all(line.startswith("Celsius:") or line.startswith("#") for line in lines[:3]):
            start_index = 1
        
        data_points = []
        for i, line in enumerate(lines[start_index:], start=start_index):
            try:
                value = float(line.split(",")[0].strip()) if "," in line else float(line.strip())
                data_points.append(value)
            except ValueError as e:
                raise ValueError(f"Invalid temperature format at line {i + 1}: {e}") from e
        
        return data_points

    except FileNotFoundError:
        raise RuntimeError(f"Input file not found: {file_path.absolute()}")
    except PermissionError:
        raise RuntimeError(f"Permission denied to read input file: {file_path.absolute()}")

def convert_celsius_to_fahrenheit(celsius_values: list[float]) -> list[float]:
    """Convert a list of Celsius temperatures to Fahrenheit."""
    return [(c * 9 / 5) + 32 for c in celsius_values]

def write_output_data(data_points: list[float], output_path, print_only=False):
    """Write converted data points to the specified path or stdout."""
    if not isinstance(output_path, Path):
        raise TypeError("Output destination must be a file path string.")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for celsius in data_points:
                f.write(f"{celsius}\n")
        
        if not print_only and output_path.exists():
            return True
        
    except PermissionError:
        raise RuntimeError(f"Permission denied to write to output file: {output_path.absolute()}")

def main():
    """Main execution block."""
    args = parse_args()

    # Generate sample data for testing without user input or files
    if args.sample_data:
        celsius_values = [0, 25.5, -10, 37, 4]
        
        output_path = Path(args.output_file) if not args.print_only else None
        
        try:
            fahrenheit_values = convert_celsius_to_fahrenheit(celsius_values)

            # Write to file or print based on flags
            if args.print_only:
                for val in fahrenheit_values:
                    print(f"{val:.2f}")
            elif output_path and not output_path.exists():
                write_output_data(fahrenheit_values, output_path, False)
            
        except Exception as e:
            raise RuntimeError("Error processing sample data.") from e

    else:
        # Process actual input file
        try:
            celsius_values = read_temperature_data(Path(args.input_file))
            fahrenheit_values = convert_celsius_to_fahrenheit(celsius_values)

            if args.print_only:
                for val in fahrenheit_values:
                    print(f"{val:.2f}")
            
            elif not output_path.exists():
                write_output_data(fahrenheit_values, Path(args.output_file), False)
                
        except Exception as e:
            raise RuntimeError("Error processing input file.") from e

if __name__ == '__main__':
    main()