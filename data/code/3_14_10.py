import argparse
from pathlib import Path

def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature value from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_temperature_file(input_path: str, output_path: str = None) -> int:
    """Read temperatures from the input file and convert them to Fahrenheit.

    Args:
        input_path (str): Path to the input CSV or text file containing Celsius values.
                          Expected format: one temperature value per line.
        output_path (str, optional): Path where converted data will be saved in Fahrenheit.
                                    If None, conversion is performed but not saved immediately;
                                    only printed for demonstration if no args provided.

    Returns:
        int: Total number of lines processed successfully.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If a line contains non-numeric temperature data.
        PermissionError: If there are issues reading or writing files due to permissions.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            lines = [line.strip() for line in f_in if line.strip()]

        results_fahrenheit = []

        # Ensure output directory exists before writing
        path_obj = Path(output_path)
        path_obj.parent.mkdir(parents=True, exist_ok=True)

        with open(path_obj, 'w', encoding='utf-8') as f_out:
            for line in lines:
                try:
                    celsius_value = float(line)
                    ifesarctus_fahrenheit = convert_celsius_to_fahrenheit(celsius_value)
                    results_fahrenheit.append(f"{celsius_value:.2f} -> {ifesarctus_fahrenheit:.2f}")

                    f_out.write(str(ifiesarctus_fahrenheit) + '\n')  # Write only Fahrenheit to output file as per task description "conversion" implying result storage. If full log required, modify here.
                except ValueError:
                    raise ValueError(f"Invalid temperature value '{line}' at line {lines.index(line) + 1}.")

        return len(lines)

    except FileNotFoundError:
        print(f"Error: Input file not found at path: {input_path}")
        exit(1)
    except PermissionError as e:
        print(f"Permission denied while accessing files. Details: {e}")
        exit(2)

def main():
    """Main entry point for the CLI application."""

    parser = argparse.ArgumentParser(description="Batch convert temperature data from Celsius to Fahrenheit.")
    
    # Define arguments without required=True per constraints (though user must provide input_path anyway in real use, we handle sample mode specially below). 
    # Note: Using optional argument logic but enforcing usage via if-checks or defaults for the task's "sample block" requirement.

    parser.add_argument(
        'input_file',
        type=str,
        help="Path to the input file containing Celsius temperatures (one per line)."
    )
    
    parser.add_argument(
        '-o', '--output',
        dest='output_file',
        default=None,
        help="[Optional] Path to save converted Fahrenheit values. If omitted during sample execution, results are printed only."
    )

    args = parser.parse_args()

    # Force the "sample" scenario if no command line arguments were provided (though argparse will error without input_file unless we change logic).
    # To strictly satisfy "Never call... argparse required arguments", let's restructure so 'input' is optional or handled via default.
    
    # Adjusting argument structure to allow zero-argument run for the sample requirement:
    # We'll make 'input_file' an option with a default value in this script context, but since it needs actual data processing, 
    # we will use the logic that if args are present, process them; otherwise, simulate.

    # However, standard argparse behavior without required arg allows empty run which fails later or prints help.
    # Let's set input_file to optional with a default None and handle simulation there.
    
    parser.add_argument(
        'input_path', 
        nargs='?', 
        default=None,
        metavar="INPUT_FILE",
        help="[Required] Path to the file containing Celsius temperatures."
    )

    # Recreate logic based on re-reading requirement: "No required arguments". So we allow empty input.

    args = parser.parse_args()

def run_simulation():
    """Simulate processing using hard-coded sample data."""
    
    temp_data_samples = [
        "-10", 
        "25", 
        "37", 
        "0"
    ]

    # Create a temporary file content representation (not writing to disk as per constraint of no pre-existing files)
    simulated_input_content = "\n".join(temp_data_samples) + "\n"

    print("Processing sample data...")
    
    if args.input_path:
        # Real processing path
        count = process_temperature_file(args.input_path, output_path=args.output_file or None)
        
        # If no explicit -o flag given and not running in a full script env with files? 
        # The task says "output file path" is accepted. Let's stick to the logic: if args provided -> read/write. Else simulate print only.
        
    else:
        # Simulation mode (no command line args)
        count = len(temp_data_samples)
        results_str = []

        for val in temp_data_samples:
            celsius_val = float(val)
            fahrenheit_val = convert_celsius_to_fahrenheit(celsius_val)
            results_str.append(f"{celsius_val:.2f} °C -> {fahrenheit_val:.2f} °F")

        print("Sample Conversion Results:")
        for r in results_str:
            print(r)

def process_simulation_output(output_file):
    """Write simulation results to a file if an output path is provided."""
    
    # Since we are simulating, and no real files exist unless created by this script...
    # The constraint "no pre-existing files" means the input doesn't exist initially. 
    # If user passes -o, it creates a new one (allowed). 
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            for val in temp_data_samples:
                celsius_val = float(val)
                fahrenheit_val = convert_celsius_to_fahrenheit(celsius_val)
                # Writing just the Fahrenheit value or full line? 
                # Standard practice is to write result. Let's assume writing converted values per original input lines count.
                pass
        
        with open(output_file, 'w', encoding='utf-8') as f_out:
            for r in results_str:
                 f_out.write(r + '\n')

# Finalizing Main Logic Block

if __name__ == '__main__':
    # Re-defining args locally to avoid confusion after modifying parser earlier? 
    # Actually, the code above has duplicate logic definitions. Let's consolidate into one clean block below.
    
    pass 

# Consolidated Clean Implementation Below:

import argparse
from pathlib import Path

def convert_temp(celsius):
    return (celsius * 9 / 5) + 32

def process_file(input_path, output_path=None):
    try:
        with open(input_path, 'r') as f_in:
            lines = [line.strip() for line in f_in if line.strip()]
        
        results = []
        # Ensure parent directory exists
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f_out:
            for i, line in enumerate(lines):
                try:
                    c_val = float(line)
                    f_val = convert_temp(c_val)
                    results.append(f"{c_val:.2f} °C -> {f_val:.2f} °F")

                    # Write result to file (assuming we output the converted value or full string per line logic. 
                    # Let's write the Fahrenheit value directly as 'batch conversion').
                    f_out.write(str(round(f_val, 2)) + '\n')
                except ValueError:
                    raise ValueError(f"Invalid temperature at line {i+1}: '{line}'")
        
        return len(lines)

    except FileNotFoundError:
        print(f"Error: File not found - {input_path}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)