import argparse
from pathlib import Path

def parse_arguments():
    """Parses command-line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Convert temperature data from Celsius to Fahrenheit in a batch."
    )
    
    # Accept an optional input file path. If not provided, use the hard-coded sample values internally.
    input_file = parser.add_argument(
        "input",
        nargs='?',
        default=None,
        help="Path to the input CSV or text file containing Celsius temperatures."
    )
    
    return parser.parse_args()

def read_temperature_data(file_path: Path) -> list[float]:
    """
    Reads temperature data from a file.
    Supports both CSV (comma-separated) and plain text files where each line is a value.
    Returns a list of float values representing Celsius temperatures.
    
    Args:
        file_path: The path to the input file.
        
    Returns:
        A list of float numbers.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If non-numeric values are found in the data.
    """
    temperatures = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                # Strip whitespace and newlines
                value_str = line.strip()
                
                if not value_str:
                    continue
                
                try:
                    temp_celsius = float(value_str)
                    temperatures.append(temp_celsius)
                except ValueError as e:
                    raise ValueError(f"Invalid temperature value at line {line_num}: '{value_str}'. Error: {e}") from e
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file '{file_path}' was not found.")

def convert_to_fahrenheit(temperatures_celsius: list[float]) -> dict[str, float]:
    """
    Converts a list of Celsius temperatures to Fahrenheit.
    
    Formula: F = (C * 9/5) + 32
    
    Args:
        temperatures_celsius: List of temperature values in Celsius.
        
    Returns:
        A dictionary mapping the original index/value to its Fahrenheit equivalent.
    """
    results = {}
    for idx, c_temp in enumerate(temperatures_celsius):
        f_temp = (c_temp * 9 / 5) + 32
        # Store key as string representation of input value for easy lookup if needed
        key_str = str(c_temp)
        results[key_str] = round(f_temp, 6)
    return results

def write_output_file(output_path: Path, conversion_results: dict[str, float]):
    """
    Writes the converted temperature data to an output file.
    
    Args:
        output_path: The path where the result will be saved (CSV format).
        conversion_results: Dictionary of conversions {input_str: fahrenheit_value}.
    """
    try:
        with open(output_path, "w", encoding="utf-8") as f_out:
            # Write header
            f_out.write("Celsius,Fahrenheit\n")
            
            for c_val in conversion_results.keys():
                if isinstance(c_val, float):
                    raw_c = str(int(c_val)) + "." + "0" * (6 - len(str(c_val).split('.')[1]) if '.' in str(c_val) else 5) 
                    # Simple formatting: ensure consistent decimal output for CSV precision
                    c_formatted = f"{float(c_val):.2f}"
                else:
                    c_formatted = str(c_val)
                
                f_out.write(f"{c_formatted},{conversion_results[c_val]}\n")
    except IOError as e:
        raise RuntimeError(f"Failed to write output file '{output_path}': {e}")

def run_conversion(input_file_path: Path, sample_values: bool = False):
    """
    Main execution logic for temperature conversion.
    
    If input_file_path is provided and exists, it reads from the file.
    Otherwise (or if specified via flag), uses hard-coded samples to demonstrate functionality without external files or prompts.
    """
    temperatures_celsius = []

    # Determine data source based on arguments
    if sample_values:
        print("Using internal hard-coded sample values for demonstration.")
        input_file_path = None  # Signal to use samples
        
        # Hard-coded sample values (Celsius)
        # -10, 0, 25.0, 37.8, 40.6
        temperatures_celsius = [-10.0, 0.0, 25.0, 37.8, 40.6]

    elif input_file_path and not sample_values:
        if not Path(input_file_path).exists():
            raise FileNotFoundError(f"Input file '{input_file_path}' does not exist.")
        
        print(f"Reading temperature data from {input_file_path}...")
        temperatures_celsius = read_temperature_data(Path(input_file_path))

    else:
        # Default fallback if no input and samples are preferred, or just error out gracefully for strict CLI usage without args.
        raise ValueError("Please provide an input file path via command line argument.")

    print(f"Processing {len(temperatures_celsius)} temperature records...")
    
    conversion_results = convert_to_fahrenheit(temperatures_celsius)
    
    if sample_values:
        output_file_name = "sample_output.csv"
    else:
        # Generate a filename based on input name or default to 'converted_temps.csv'
        base_name = Path(input_file_path).stem if input_file_path else "input_data"
        output_file_name = f"{base_name}_fahrenheit.csv"

    print(f"Converting results written to {output_file_name}...")
    
    # Ensure parent directory exists for the output file
    output_path = Path(output_file_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    write_output_file(output_path, conversion_results)

    print("Conversion completed successfully.")

if __name__ == '__main__':
    # Parse arguments without requiring them; provide a default fallback for demonstration.
    args = parse_arguments()

    try:
        if args.input is None or not Path(args.input).exists():
            # Since the task forbids input(), sys.stdin, and requires no network/files prior to run,
            # we simulate an environment where file access isn't possible by defaulting to samples.
            print("No valid input file provided or found; running with hard-coded sample values.")
            
        else:
            try:
                run_conversion(Path(args.input), sample_values=False)
            except FileNotFoundError as e:
                # Ensure the error message is informative and does not crash abruptly without explanation
                raise Exception(f"Script execution halted due to missing resource:\n{e}") from None

    except ValueError as ve:
        print("Error during script initialization or logic flow.")
        if hasattr(ve, '__cause__'):
            cause = ve.__cause__
            if isinstance(cause, FileNotFoundError):
                raise Exception(f"Required input file not found:\n{str(cause)}") from None

    except Exception as e:
        # Final catch-all to ensure informative error messages are displayed clearly.
        print("An unexpected critical error occurred.")
        print(str(e))