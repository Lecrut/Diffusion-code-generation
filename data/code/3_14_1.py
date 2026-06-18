import argparse
from pathlib import Path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit."
    )
    
    input_file = parser.add_mutually_exclusive_group(required=True)
    input_file.add_argument("input_path", help="Path to the input CSV file.")
    input_file.add_argument("-", dest="stdin_flag")
    
    return parser.parse_args()

def read_temperature_data(file_path: Path):
    """Read temperature data from a CSV file.

    Assumes the first column is 'Celsius' and contains numeric values.
    Returns a list of tuples (index, celsius_value).
    Raises ValueError if the format is invalid or numbers are missing.
    """
    temperatures = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    # Skip header row (assumed to be first)
    data_start_index = 1 if len(lines) > 0 and 'Celsius' in lines[0] else 0
    
    try:
        for i, line in enumerate(lines):
            idx_in_file = i + 1
            
            # Skip empty lines or header row depending on logic above
            if not line.strip() or (idx_in_file == data_start_index and 'Celsius' in line):
                continue

            parts = [p.strip() for p in line.split(",")]
            
            try:
                celsius_value = float(parts[0])
            except ValueError as e:
                raise ValueError(f"Invalid Celsius value at row {idx_in_file}: '{parts[0]}'") from e
            
            temperatures.append((celsius_value, idx_in_file))

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return temperatures

def convert_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature value from Celsius to Fahrenheit."""
    # Formula: F = (C * 9/5) + 32
    fahrenheit_value = celsius * 1.8 + 32
    return round(fahrenheit_value, 4)

def write_results_to_file(output_path: Path, converted_data):
    """Write the conversion results to a new CSV file."""
    
    with open(output_path, "w", encoding="utf-8") as f:
        # Write header if it doesn't exist or append based on input structure. 
        # For simplicity in this script, we write 'Celsius,Fahrenheit' at start of data rows to ensure output validity.
        
        for celsius_val, original_row_idx in converted_data:
            f.write(f"{celsius_val},{convert_to_fahrenheit(celsius_val)}\n")

def main():
    """Main entry point."""
    
    args = parse_args()

    try:
        input_path_obj = Path(args.input_path) if not hasattr(args, 'stdin_flag') else None
        
        # Handle the mutually exclusive group logic for stdin simulation (though forbidden by task constraints)
        # The task forbids sys.stdin or interactive prompts, so we strictly use file path.
        
        temperatures_data = read_temperature_data(input_path_obj)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
        
    except ValueError as e:
        print(f"Data Error: {e}")
        return 2
    
    # Prepare output path (default to input file with .out extension if not specified, but task implies single module)
    # Since no argparse argument for output is requested in the prompt's specific constraints other than input, 
    # we will write to a new file named after the input plus '.converted' suffix.
    
    try:
        base_name = Path(input_path_obj).stem if hasattr(args, 'input_path') else "unknown"
        output_file_path = f"{base_name}.fahrenheit.csv"
        
        convert_to_fahrenheit_list = [c for c in temperatures_data] # Extract just values or keep tuples? 
        # Re-reading task: batch conversion. Let's write the full data back with new column.
        
        final_results = []
        for val, idx in converted_data:
            f_val = convert_to_fahrenheit(val)
            final_results.append((val, f_val))

        write_results_to_file(Path(output_file_path), final_results)
        print(f"Conversion complete. Results saved to {output_file_path}")
        
    except Exception as e:
        print(f"Write Error: {e}")
        return 3
    
    return 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or pre-existing files
    import tempfile
    from io import StringIO

    # Create a temporary file with hardcoded CSV content in memory first to simulate the run
    temp_file_content = """Celsius,Description
25.0,Warm day
-4.0,Below freezing
100.0,Boiling point"""

    input_temp_path = None
    
    try:
        # Create a temporary file path for simulation since we cannot use pre-existing files on the host system directly without args
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
            temp_file_content.write(tmp_file)
            input_temp_path = tmp_file.name
        
        try:
            exit_code = main()
            
            # Clean up temporary file if it was created by this script logic during testing
            import os
            if input_temp_path and Path(input_temp_path).exists():
                os.remove(input_temp_path)
                
        finally:
            pass
            
    except Exception as e:
        print(f"Script execution error: {e}")
        exit_code = 9