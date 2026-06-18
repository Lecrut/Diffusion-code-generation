import argparse
from pathlib import Path

def parse_temperature(value: str) -> float:
    """Convert a string temperature value to a float."""
    try:
        return float(value.strip())
    except ValueError as e:
        raise ValueError(f"Invalid numeric input '{value}': {e}") from None

def celsius_to_fahrenheit(celsius: float) -> tuple[float, str]:
    """Convert Celsius temperature to Fahrenheit and return the result with status."""
    fahrenheit = (celsius * 9 / 5) + 32
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Temperature conversion failed due to non-numeric output.")
    
    # Check for NaN or Inf which might occur during calculation errors in some contexts
    import math
    if math.isnan(fahrenheit) or math.isinf(fahrenheit):
        return fahrenheit, "Error: Invalid temperature value (NaN/Inf detected)"
    
    status = "OK"
    try:
        # Attempt to format the number; this might fail for extremely large/small numbers
        formatted_f = "{:.2f}".format(fahrenheit)
    except Exception as e:
        return fahrenheit, f"Error during output formatting: {e}"
    
    return float(formatted_f), status

def process_file(input_path: Path) -> None:
    """Read the input file line by line and convert temperatures."""
    if not input_path.exists():
        raise FileNotFoundError(f"The file '{input_path}' does not exist.")

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        converted_results = []
        for line_num, line in enumerate(lines, start=1):
            original_line = line.strip()
            
            # Skip empty lines or comments (lines starting with #)
            if not original_line or original_line.startswith('#'):
                continue
            
            try:
                celsius_value = parse_temperature(original_line)
                fahrenheit_value, status_msg = celsius_to_fahrenheit(celsius_value)
                
                converted_results.append({
                    'original': original_line,
                    'converted': str(fahrenheit_value),
                    'status': status_msg
                })
            except ValueError as e:
                # Handle cases where the line is not a valid number but isn't empty/commented
                error_prefix = f"Line {line_num}: " if len(original_line) > 0 else ""
                converted_results.append({
                    'original': original_line,
                    'converted': "",
                    'status': f"{error_prefix}Error parsing temperature: {e}"
                })

        # Write results to a new file with the same name but .txt extension (or overwrite if desired)
        output_path = Path(f"temp_conversion_{input_path.name}")
        
        try:
            with open(output_path, 'w', encoding='utf-8') as out_f:
                for item in converted_results:
                    # Format the line based on status to avoid overwriting original data if it was an error
                    output_line = f"{item['original']} -> {item['converted']}\t[{item['status']}] " + "\n"
                    out_f.write(output_line)
            print(f"Conversion complete. Results written to: {output_path}")
        except PermissionError as e:
            raise RuntimeError(f"Failed to write output file '{output_path}': {e}") from None

    except IOError as e:
        raise RuntimeError(f"IO error while processing file '{input_path}': {e}") from None

def main():
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage: python temp_converter.py input_file.txt
""",
        add_help=False  # We will handle help manually if needed or let it be default
    )

    parser.add_argument(
        'input',
        type=str,
        help="Path to the input file containing Celsius temperatures."
    )
    
    args = parser.parse_args()
    
    try:
        process_file(Path(args.input))
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except RuntimeError as e:
        print(f"Runtime error occurred: {e}")
        return 1
    
    # If no errors, exit with success code (though argparse usually handles help)
    if args.input == '--help':
        parser.print_help()
    
    return 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    # We simulate a file processing scenario by creating a temporary in-memory dataset 
    # and writing it to a temp file, then processing that temp file immediately.
    
    import tempfile
    
    # Create a temporary directory for this isolated execution
    with tempfile.TemporaryDirectory() as tmp_dir:
        input_file = Path(tmp_dir) / "sample_temps.txt"
        
        # Write sample data directly to the temp file (no network, no stdin required)
        sample_data = [
            "# Sample temperature dataset",
            "25.0",
            "-10.5",
            "37.8",
            "",  # Empty line
            "invalid_input",
            "40.0"
        ]
        
        with open(input_file, 'w', encoding='utf-8') as f:
            for item in sample_data:
                if item.strip():  # Only write non-empty lines to the file content logic-wise, 
                                  # though we expect empty lines might be skipped by process_file anyway.
                    f.write(item + '\n')
        
        # Run the conversion on this specific temp file path
        exit_code = main()
    
    print(f"Script execution finished with code: {exit_code}")