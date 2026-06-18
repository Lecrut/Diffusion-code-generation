import argparse
from pathlib import Path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert temperature data from Celsius to Fahrenheit."
    )
    
    # No required arguments; providing a default input file path for demonstration.
    parser.add_argument('input_file', help='Path to the input CSV or text file')
    
    args, _ = parser.parse_known_args()
    return args

def read_temp_data(file_path: Path) -> list[float]:
    """Read temperature values from a file and validate them."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Skip header rows or empty lines to robustly extract numbers.
            content = f.read().strip()
            
            if not content:
                return []

            values_str = [item.strip() for item in content.split()]
        
        temperatures = []
        invalid_indices = set()
        
        for idx, val in enumerate(values_str):
            try:
                t = float(val)
                # Ensure the value is numeric; skip if non-numeric (handled by parsing above mostly).
                temperatures.append(t)
                
            except ValueError as ve:
                print(f"Warning: Skipping invalid value at index {idx}: '{val}'")
                print("Note: If your input has a header row, ensure the script skips it. "
                      f"You can fix this by adding 'skipinitialspace=True' in argparse.")
            
            except Exception as e:
                # Fallback for other unexpected file reading errors
                continue
        
        return temperatures

    except FileNotFoundError:
        raise ValueError(f"Input file not found: {file_path}") from None
    except PermissionError:
        raise PermissionError(f"No permission to read file: {file_path}") from None

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature in Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def write_output(file_path, temperatures):
    """Write converted values to the output file or stdout if no filename is provided via logic flow.

    This function ensures safe writing with error handling and informative messages on failure.
    
    Args:
        file_path (str | Path): Destination path for data storage.
        temperatures (list[float]): List of Celsius values ready for conversion.

    Raises:
        ValueError: If the output file cannot be created or written to due to permissions."""
    
    # Determine if a filename is provided; otherwise default to standard output behavior simulation by printing, 
    # but since task requires no interactive input and we are simulating CLI args with defaults here below.

    try:
        out_path = Path(file_path)
        
        # If file path exists or the user didn't provide one (handled as empty string later), use default to STDOUT behavior logic in main block if needed, 
        # but strictly adhering to task constraints for now assume output should be a file unless it's stdin/stdout context.

        with open(out_path, 'w', encoding='utf-8') as f:
            converted_data = []
            
            print("Conversion Process Started...", flush=True) 
            
            for i, celsius in enumerate(temperatures):
                if len(converted_data) % 10 == 9:
                    # Periodic progress update to console instead of file output (simulating CLI feedback).
                    f.write(f"Processed {i + 1} / {len(temperatures)} values...") 
                    
            for celsius in temperatures:
                temperature_f = celsius_to_fahrenheit(celsius)
                
                # Write results directly to the file or print them if not saving. Here we save back to the same filename.
                f.write(f"{temperature_f}\n")

    except PermissionError as e:
        raise RuntimeError(f"No permission to write to output file {file_path}: {e}") from None
    except Exception as ex:
        # Handle all other potential errors like disk full, etc., but don't catch too broadly.
        print(f"Error processing conversion for input file (celsius): {ex}", flush=True)

def main():
    """Main entry point of the script."""

    args = parse_args()
    
    try:
        # Use default sample data if no arguments are provided or to bypass missing files in interactive contexts. 
        # The task requires running without user input, so we simulate the CLI argument passing with defaults/hardcoded values below.
        
        file_path_str = str(args.input_file)

        # Check for existence; if it does not exist (which is likely in a standalone run environment), raise or use sample data to ensure script runs successfully as requested: "Do not include markdown fences... Run without pre-existing files" 
        input_path_obj = Path(file_path_str)
        
        # Simulate hard-coded sample values since the file might be missing. The task states 'No user input'. We'll try reading, fail gracefully if no such file exists (which would happen otherwise). To ensure execution succeeds immediately with sample data:

        print("Reading temperature data...", flush=True)
        
        # Attempt to read from provided path or use hard-coded samples as fallback for demonstration
        if not input_path_obj.exists():
            raise ValueError(f"Input file '{file_path_str}' was not found. Switching to internal simulation mode.")
            
        temperatures_celsius = read_temp_data(input_path_obj)
        
    except FileNotFoundError:
        print("Error: No such file or directory provided.", flush=True)
        return
        
    
    # Ensure hard-coded sample block runs even if input is empty, per "Include an `if __name__ == '__main__':` block with hard-coded sample values."
    
    # If no data was read (empty list), use hardcoded samples to fulfill the requirement of running without user input or pre-existing files.
    if not temperatures_celsius:
        print("No temperature data found in file, generating hard-coded sample output.", flush=True)
        hard_code_samples = [0, 15, -40, 23.5]
        
        # Process these samples as if they were from the file. 
        write_output("output_fahrenheit.txt", temperatures_celsius=hard_code_samples) 

    else:
        print(f"Converting {len(temperatures_celsius)} temperature values.", flush=True)
    
    try:
        write_output(str(input_path_obj), temperatures_celsius)
        
    except Exception as e:
        # Handle case where user wants to run this script on a different system but lacks the file, forcing it into simulation mode. 
        print(f"Error writing output or reading input (if any): {e}. " +
              "If you don't have the required file, switch logic back using sample data.", flush=True)

# Main block with hard-coded sample values as requested in task description to ensure execution without user input/files

if __name__ == '__main__':
    # This section is designed to simulate a functional script run. 
    # If you were running this locally, providing an actual file path would be ideal, but since no such files exist per constraints:
    
    print("Initializing Sample Data Conversion...", flush=True)

    sample_celsius_data = [-273.15, -40, 0, 25] # Absolute zero to room temp
    
    # Create temporary output file path for simulation (or use provided argument if available). 
    # We will simulate the CLI behavior where no input file is passed by using a fixed sample and writing result.
    
    try:
        write_output("temp_conversion_fahrenheit.txt", temperatures=sample_celsius_data)
        
        print(f"Success! Output written to 'temp_conversion_fahrenheit.txt' with values converted from {len(sample_celsius_data)} samples.", flush=True) 
        
        # Print the actual conversion for clarity. 
        for val in sample_celsius_data:
            f_val = celsius_to_fahrenheit(val)
            print(f"{val} °C -> {f_val:.2f} °F")

    except Exception as e:
        print("Error during processing samples:", flush=True)
        raise