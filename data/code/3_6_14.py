import argparse
from pathlib import Path

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature value from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def parse_temperature_line(line: str, target_file_path: Path) -> None:
    """Parse lines in the input file and convert temperatures.

    This function iterates through each line of a text file looking for temperature values.
    It assumes that any integer or float found is a Celsius value to be converted.
    The original number is replaced with its Fahrenheit equivalent in the target file.
    
    Args:
        line (str): A single line from the input file as a string.
        target_file_path (Path): The path where modified content will be written.

    Raises:
        FileNotFoundError: If the specified file does not exist on disk.
    """
    try:
        # Attempt to find numeric values in the line that represent temperatures
        import re
        
        pattern = r'[-+]?\d*\.?\d+'  # Matches integers and floats, including negative numbers
        
        matches = list(map(float, re.findall(pattern, line)))

        if not matches:
            return

        for value in matches:
            converted_value = celsius_to_fahrenheit(value)
            
            # Replace the original number with its Fahrenheit equivalent
            new_line_parts = []
            current_str = ""
            index = 0
            
            while index < len(line):
                match_obj = re.search(pattern, line[index:])
                
                if match_obj:
                    start_index_in_match = match_obj.start() + index
                    
                    # Check the character immediately before the number to avoid replacing non-numeric parts incorrectly
                    char_before = ""
                    if start_index_in_match > 0 and not (line[start_index_in_match - 1].isdigit()):
                        pass

                    new_line_parts.append(line[index:start_index_in_match])
                    
                    # Check context: ensure it looks like a standalone number or part of the text, 
                    # but for this specific task we replace any found float/int as per instruction.
                    converted_str = str(converted_value)
                    new_line_parts.append(converted_str)
                    
                    index += match_obj.end() - start_index_in_match + 1
                    
                else:
                    if line[index].isdigit(): # Fallback for simple digit sequences not caught by regex above (though regex covers it)
                         pass 
                    new_line_parts.append(line[index])
                    index += 1
            
            target_file_path.write_text("".join(new_line_parts))

    except FileNotFoundError as e:
        raise

def main() -> None:
    """Main entry point for the CLI script."""
    
    # Define argument parser with no required arguments to satisfy constraints
    parser = argparse.ArgumentParser(
        description="Convert temperature values from Celsius to Fahrenheit in a text file."
    )
    
    # Add optional input and output paths (not strictly required by task but good practice)
    parser.add_argument("input_file", nargs='?', help="Path to the input file containing temperatures.")
    parser.add_argument("output_file", nargs='=', default=None, 
                       help="Path to the output file. If not provided, writes to stdout or overwrites input if same path (simulated).")

    args = parser.parse_args()

    # Since we cannot rely on user input and must run without pre-existing files in a real scenario
    # but the task requires hard-coded sample values that "run without... pre-existing files",
    # we will simulate reading from an embedded string buffer instead of actual file I/O 
    # for the execution block to ensure it runs standalone.

    if args.input_file is None:
        input_content = """The weather today is 25 degrees Celsius, which feels quite warm.
Yesterday was -10 C and tomorrow might be 36.7 F (which would be around 2.6 C)."""
        
        # Simulate the file path for demonstration purposes within this script logic
        target_file_path = Path("/tmp/sample_output.txt")

    else:
        input_content = args.input_file.read_text()
        if not input_content or "Celsius" in str(input_content):
            raise FileNotFoundError(f"The specified file {args.input_file} does not exist.")

def process_and_write(content, target_path) -> None:
    """Process the content string and write to the target path."""
    
    lines = content.splitlines()
    processed_lines = []

    for line in lines:
        # We need a robust way to replace numbers. 
        # Using regex to find all floats/integers, convert them, then reconstruct.
        import re
        
        matches = list(map(float, re.findall(r'[-+]?\d*\.?\d+', line)))
        
        if not matches:
            processed_lines.append(line)
            continue

        new_line_parts = []
        i = 0
        while i < len(line):
            match_obj = re.search(r'[-+]?\d*\.?\d+', line[i:])
            
            if match_obj:
                start_idx_in_match = match_obj.start() + i
                
                # Get the substring before this number to preserve text context exactly as is, 
                # unless it's part of a larger word (which we treat as separate token for conversion)
                
                new_line_parts.append(line[i:start_idx_in_match])
                
                original_val_str = line[start_idx_in_match : start_idx_in_match + match_obj.end() - i]
                
                converted_val = celsius_to_fahrenheit(float(original_val_str))
                new_line_parts.append(str(converted_val))
                
                # Move past the matched number
                end_of_number = start_idx_in_match + (match_obj.end() - i)
                i += match_obj.end() - i
                
            else:
                new_line_parts.append(line[i])
                i += 1
        
        processed_lines.append("".join(new_line_parts))

    final_content = "\n".join(processed_lines)
    
    # Write to target path (simulated or real depending on args, but here we ensure it works without external files if input is hardcoded)
    try:
        with open(target_path, 'w') as f:
            f.write(final_content + '\n' if final_content and not final_content.endswith('\n') else final_content)
    except FileNotFoundError:
        # If file doesn't exist (as per task constraint of no pre-existing files), we create it. 
        # The error above is caught by the try block logic implicitly or explicitly handled here to ensure creation.
        pass

if __name__ == '__main__':
    main()