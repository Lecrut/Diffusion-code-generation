import argparse

def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9) / 5 + 32

def process_file(file_path, output_func=None):
    """Process lines in the file and convert temperatures.
    
    Args:
        file_path: Path to input text file containing numbers representing 
                   temperature values in Celsius.
        output_func (optional): Function that modifies line content based on conversion.
                               If None, prints converted value directly.
    
    Returns:
        List of modified lines if output_func is provided.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        processed_lines = []
        for line in lines:
            stripped_line = line.strip()
            
            # Check if the line is a valid integer or float representing temperature
            try:
                temp_value = float(stripped_line)
                
                # Convert to Fahrenheit and format back to string (preserve decimal places roughly)
                fahrenheit_temp = celsius_to_fahrenheit(temp_value)
                
                # Format output with sufficient precision for comparison
                formatted_output = str(round(fahrenheit_temp, 2)) if temp_value != int(temp_value) else str(int(fahrenheit_temp))
            except ValueError:
                # If conversion fails (e.g., not a number), keep original line
                processed_lines.append(stripped_line)
                continue
            
            processed_lines.append(formatted_output)

        return processed_lines, True  # Indicate success
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Convert temperature values from Celsius to Fahrenheit.')
    parser.add_argument('input_file', help='Path to the input file containing temperatures in Celsius')
    args = parser.parse_args()

    processed_lines, success = process_file(args.input_file)
    if not success:
        exit(1)

    # Write results back to same file or print them
    with open(args.input_file, 'w', encoding='utf-8') as f:
        for line in processed_lines:
            f.write(line + '\n')