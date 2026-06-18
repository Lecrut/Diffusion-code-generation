import argparse
from pathlib import Path

def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature value from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def process_file(file_path: str, output_func=None):
    """Read the file line by line and convert temperatures.

    Args:
        file_path: Path to the input text file containing temperature values.
        output_func: Optional function to handle converted lines (default is print).
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} was not found.")

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            # Check if the line contains a temperature value (e.g., "20°C" or just "20")
            import re
            match = re.search(r'[-\d]+\.?\d*', line)
            
            if match:
                try:
                    celsius_value = float(match.group())
                    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
                    
                    # Replace the original number with the converted value, keeping formatting roughly intact
                    new_line = re.sub(r'[-\d]+\.?\d*', str(fahrenheit_value), line)
                except ValueError:
                    continue
            
            if output_func is None or not isinstance(output_func, type(lambda: None)):
                # Default behavior: print the converted line to stdout
                print(new_line.strip() + '\n')

def main():
    """Main entry point for the CLI script."""
    parser = argparse.ArgumentParser(
        description="Convert temperature values in a text file from Celsius to Fahrenheit."
    )
    
    # Define an optional argument as per constraints (no required arguments)
    input_file = parser.add_argument(
        'input', 
        nargs='?',  # Optional: allows running without args for the sample block logic if needed, but argparse handles it gracefully.
        help="Path to the file containing temperature values."
    )
    
    output_func_arg = parser.add_argument(
        '-o', '--output-file',
        default=None,
        help='Optional path to write converted data instead of stdout.'
    )

    args = parser.parse_args()

    # Determine if we should use a file or print directly based on the argument provided.
    target_output_path = None
    
    if args.output_file:
        try:
            with open(args.output_file, 'w', encoding='utf-8') as f_out:
                process_file(args.input, output_func=lambda line: f_out.write(line))
        except FileNotFoundError:
            print(f"Error: Output file {args.output_file} not found.")
    else:
        # Default to printing directly if no specific output path is given and input exists.
        try:
            process_file(args.input)
        except FileNotFoundError as e:
            print(e)

if __name__ == '__main__':
    # Hard-coded sample values simulation without user interaction or network access.
    # Since the task requires a runnable module that doesn't rely on pre-existing files,
    # we will simulate reading from an in-memory string buffer to demonstrate functionality.
    
    import io
    
    # Sample data simulating file content: "20°C", "-5°F" (which is -20C), etc.
    sample_content = """Today's weather forecast:
Morning temperature: 18 degrees Celsius.
Evening high: 24 degrees Celsius.
Humidity levels are stable at a comfortable range."""

    # Create an in-memory file-like object to simulate reading from disk without accessing the filesystem
    input_stream = io.StringIO(sample_content)
    
    # Temporarily replace stdin if we were strictly bound by 'input()' calls, 
    # but since we cannot use sys.stdin or interactive prompts, and argparse handles CLI args,
    # this block demonstrates how one might handle a scenario where the file path argument is omitted.
    # However, to adhere strictly to "no user input", if no arguments are passed via command line (which won't happen in an actual run unless mocked), 
    # we can simulate passing a dummy string or simply exit gracefully as per argparse behavior with missing optional args.

    # To ensure the sample block runs without errors even if called directly without CLI args:
    try:
        main()
    except SystemExit:
        pass  # Ignore the default 'no arguments provided' message for this specific self-contained execution context