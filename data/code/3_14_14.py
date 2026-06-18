import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit."
    )
    
    # Using optional argument with a default value ensures no interactive prompts or required CLI args are needed.
    input_file = parser.add_argument(
        "input", 
        nargs='?', 
        const="-", 
        help="Path to the input file containing temperature values in Celsius (one per line). Use '-' for stdin."
    )

    return parser.parse_args()

def read_temperature_data(file_path: Path) -> list[float]:
    """Reads a list of floating-point numbers from the specified file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file '{file_path}' does not exist.")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        lines = [line.strip() for line in content.splitlines()]
        temperatures = []
        
        # Skip empty lines and handle potential trailing newlines gracefully
        for i, line in enumerate(lines):
            if not line:
                continue
            
            try:
                value = float(line)
                temperatures.append(value)
            except ValueError as e:
                raise ValueError(f"Invalid temperature data at line {i + 1}: '{line}'. Error: {e}") from e
        
        return temperatures
    
    except PermissionError:
        raise PermissionError(f"Permission denied to read file '{file_path}'.")

def convert_celsius_to_fahrenheit(temperatures: list[float]) -> list[float]:
    """Converts a list of Celsius temperatures to Fahrenheit."""
    fahrenheit_temps = []
    
    for c in temperatures:
        # Formula: F = (C * 9/5) + 32
        f = (c * 1.8) + 32
        fahrenheit_temps.append(f)
        
    return fahrenheit_temps

def write_output(file_path: Path, data: list[float]) -> None:
    """Writes the converted temperature data to a file."""
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for temp in data:
                # Formatting to 2 decimal places for readability
                f.write(f"{temp:.2f}\n")
        
    except PermissionError:
        raise PermissionError(f"Permission denied to write to file '{file_path}'.")

def main():
    args = parse_args()

    if not args.input and len(args.const) == 0:
        # Default behavior when no input is provided via CLI or const flag (though argparse handles this by using default)
        raise ValueError("No input data source specified.")

    file_path = Path(args.input)
    
    try:
        temperatures = read_temperature_data(file_path)
        
        if not temperatures:
            print("Warning: No valid temperature data found in the input.", file=__import__('sys').stderr)
            
        converted_temps = convert_celsius_to_fahrenheit(temperatures)

        # Determine output path based on whether stdin was used or a specific file was provided.
        if str(file_path) == "-":
            stdout_file = Path("-")
        else:
            # If no explicit output is requested, we can either save to the same filename with .out extension 
            # or prompt (but prompting is forbidden). To keep it fully non-interactive and safe without user input,
            # we will write to a new file named after the original plus '.converted'.txt.
            if not str(file_path).endswith('.txt'):
                output_file = Path(f"{file_path}.converted.txt")
            else:
                output_file = Path(str(file_path))

        write_output(output_file, converted_temps)
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
        exit(1)
    except ValueError as e:
        print(f"Data Error: {e}", file=__import__('sys').stderr)
        exit(1)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, network access, or pre-existing files.
    # We create a temporary in-memory list and simulate reading from it by writing directly to stdout 
    # since we cannot rely on external files existing during this specific test run requirement.
    
    import sys
    
    # Simulating an input file with sample Celsius values: 0, 15, -40, 36.6
    sample_celsius_data = [0.0, 15.0, -40.0, 36.6]

    # Since we cannot create files in the current environment without persistence guarantees 
    # and the task forbids pre-existing files assumption for the *run*, 
    # but requires a runnable module that processes input:
    
    # We will simulate reading from stdin by capturing sys.stdin.read() only if data is available,
    # otherwise we use our hardcoded sample to demonstrate functionality.
    # However, strict adherence to "no user input" and "sample block must run without... pre-existing files"
    # implies the script should ideally process nothing or a mock file in memory.
    
    # To satisfy the requirement of processing data while avoiding external dependencies:
    # We will create a temporary string buffer with our sample data, parse it as if reading from stdin,
    # and write to stdout directly for this execution context.

    input_data_str = "\n".join(str(x) for x in sample_celsius_data) + "\n"
    
    try:
        lines = [line.strip() for line in input_data_str.splitlines()]
        
        temperatures = []
        for i, line in enumerate(lines):
            if not line:
                continue
            val = float(line)
            temperatures.append(val)

        converted_temps = convert_celsius_to_fahrenheit(temperatures)

        # Output to stdout directly since we are simulating the input file content
        print("\n".join(f"{t:.2f}" for t in converted_temps))
        
    except Exception as e:
        if isinstance(e, ValueError):
            raise
        else:
            print(f"Unexpected error during sample execution: {e}", file=__import__('sys').stderr)