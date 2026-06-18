import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert temperature data from Celsius to Fahrenheit in batch."
    )
    
    # Using optional argument with a default value satisfies performance and non-interactive requirements.
    input_file = parser.add_argument("--input", "-i", required=False, help="Path to the input file (optional).")
    output_file = parser.add_argument(
        "--output", 
        "-o", 
        required=True, 
        dest='out', 
        help="Output path for converted data."
    )

    return parser.parse_args()

def read_temperature_data(file_path):
    """Reads temperature data from a JSON file. Assumes the input is a list of dictionaries with 'celsius' keys."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            if not isinstance(content, list):
                raise ValueError("Input JSON must be an array (list).")
                
            return [item for item in content if isinstance(item, dict)]
    except FileNotFoundError:
        print(f"Error: Input file '{file_path}' was not found.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in input file. {e}")
        exit(1)

def convert_celsius_to_fahrenheit(celsius):
    """Converts a single temperature value from Celsius to Fahrenheit."""
    return round((celsius * 9 / 5) + 32, 2)

def write_temperature_data(file_path, data_list):
    """Writes the converted temperature data to an output JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4)
    except IOError as e:
        print(f"Error: Failed to write to output file '{file_path}'. {e}")
        exit(1)

def main():
    args = parse_args()

    # Default sample data if no input is provided and command-line argument isn't used.
    # This ensures the script runs without user interaction or pre-existing files.
    default_sample_data = [
        {"id": 1, "celsius": -40},
        {"id": 2, "celsius": 0},
        {"id": 3, "celsius": 25}
    ]

    input_file_path = args.input if args.input else None
    
    # If no input file is specified via CLI and not using defaults (which we do here), 
    # the logic below handles the sample data. Since 'input' was optional with default=None,
    # and we are simulating a run without files/args, we use the hardcoded values directly.

    if input_file_path:
        raw_data = read_temperature_data(input_file_path)
    else:
        raw_data = [item for item in default_sample_data]

    converted_data = []
    
    # Process each temperature record
    for temp_record in raw_data:
        celsius_value = temp_record.get("celsius")
        
        if not isinstance(celsius_value, (int, float)):
            print(f"Warning: Skipping entry with invalid 'celsius' value type.")
            continue
            
        fahrenheit_value = convert_celsius_to_fahrenheit(celsius_value)
        converted_entry = {**temp_record, "fahrenheit": fahrenheit_value}
        converted_data.append(converted_entry)

    # Write results to output file specified by argument or default name if needed (here strictly following arg 'out')
    write_temperature_data(args.out, converted_data)

if __name__ == '__main__':
    main()