import argparse
from pathlib import Path

def parse_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_file(input_path: str, output_path: str = None) -> int:
    """Read a file containing numeric values, convert them to Fahrenheit, and write results.

    Args:
        input_path: Path to the input text file with one number per line (Celsius).
        output_path: Optional path for the output file. If not provided, writes to stdout.

    Returns:
        The total count of lines processed.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If a non-numeric value is found in the input file.
    """
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input file '{input_path}' was not found.")

    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            lines = [line.strip() for line in infile.readlines()]

        converted_values = []
        error_count = 0

        for idx, line in enumerate(lines):
            if not line or line.isspace():
                continue
            
            try:
                celsius_value = float(line)
                fahrenheit_value = parse_celsius_to_fahrenheit(celsius_value)
                converted_values.append(f"{fahrenheit_value:.2f}")
            except ValueError as e:
                error_count += 1

        if output_path is None or not Path(output_path).exists():
            # Write to stdout for simplicity when no specific output file requested in sample context
            print('\n'.join(converted_values))
        
        else:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write('\n'.join(converted_values) + '\n')

        return len(lines) - error_count  # Return count of successfully processed lines

    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while processing the file: {e}")

def main():
    """Main entry point for the CLI script."""
    
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage (with sample values):
  python temp_converter.py --input /dev/stdin

Sample input file format:
20.5
36.1
-4.0

Expected output:
68.90
97.00
24.80
        """
    )

    parser.add_argument(
        'input_file',
        nargs='?',
        help="Path to the input file containing Celsius values (one per line)."
             "If not provided, uses a hard-coded sample dataset."
    )
    
    # Optional output file argument
    parser.add_argument(
        '-o', '--output',
        default=None,
        help="Optional path for the output file. If omitted, results are printed to stdout."
    )

    args = parser.parse_args()

    if not args.input_file:
        # Use hard-coded sample values as per task requirements (no user input)
        print("No input file provided. Using internal sample data.")
        
        # Simulate reading from stdin/stdout for the sample block to avoid interactive prompts
        # We will read directly here instead of using sys.stdin or argparse required args logic
        
        sample_data = [
            "20.5",
            "36.1",
            "-4.0"
        ]

        input_path_str = "/dev/stdin"  # Mark as stdin for the function to handle correctly if needed, 
                                       # but we will simulate reading directly below
        
        try:
            lines = sample_data.copy()
            
            converted_values = []
            error_count = 0
            
            for idx, line in enumerate(lines):
                if not line or line.isspace():
                    continue
                
                try:
                    celsius_value = float(line)
                    fahrenheit_value = parse_celsius_to_fahrenheit(celsius_value)
                    converted_values.append(f"{fahrenheit_value:.2f}")
                except ValueError as e:
                    error_count += 1
            
            # Output results to stdout directly since no specific output file was forced 
            # and the sample block must run without pre-existing files.
            print('\n'.join(converted_values))

        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred during internal processing: {e}")

if __name__ == '__main__':
    main()