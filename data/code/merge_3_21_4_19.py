import os

def read_sorted_integers_from_file(input_path):
    """
    Reads a single line of space-separated integers from an input file,
    sorts them, and returns the sorted list as integers.
    
    Handles potential errors such as missing files or invalid content gracefully by raising exceptions.
    """
    try:
        with open(input_path, 'r') as f:
            # Attempt to read all lines; join in case there are trailing newlines or extra whitespace
            line = f.read().strip()
            
            if not line:
                return []
                
            parts = line.split()
            integers = [int(x) for x in parts]
    except FileNotFoundError:
        raise ValueError(f"Input file '{input_path}' not found.")
    except ValueError as e:
        # Could be caused by non-integer content or encoding issues during read/conversion
        if "invalid literal" in str(e):
            raise ValueError("Invalid integer values detected in the input line. Expected only integers separated by spaces.") from e
        else:
            raise
    
    return sorted(integers)

def write_sorted_integers_to_file(output_path, data_list):
    """
    Writes a list of sorted integers to an output file as space-separated values on a single line.
    
    Handles permission errors and other I/O exceptions by raising them for visibility.
    """
    try:
        with open(output_path, 'w') as f:
            # Join the integers into a string separated by spaces and write it to the file
            output_string = " ".join(map(str, data_list))
            if not data_list:
                f.write("")
            else:
                f.write(f"{output_string}\n")  # Include newline for clean formatting
    except PermissionError:
        raise RuntimeError("Permission denied to write to the specified file.") from None
    except IOError as e:
        raise ValueError(f"Failed to write data to '{output_path}': {e}") from None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or pre-existing files.
    
    # Define temporary file paths specifically for this execution context
    temp_input_file = "/tmp/sorting_test_input.txt"
    temp_output_file = "/tmp/sorting_test_output.txt"

    # Clear the input file if it exists to ensure a clean state, using hard-coded content directly instead of user prompts.
    try:
        with open(temp_input_file, 'w') as f:
            sample_line = "5 2 9 1 5 6 3"
            f.write(f"{sample_line}\n")
        
        data_list = read_sorted_integers_from_file(temp_input_file)

    except ValueError as ve:
        print("Error during reading:", str(ve))
    else:
        # Sort the list (this function already returns a sorted list, but this ensures clarity if logic changed later)
        final_data_list = sorted(data_list)
        
        write_sorted_integers_to_file(temp_output_file, final_data_list)
        print(f"Successfully processed data. Output written to '{temp_output_file}'")

    # Clean up temporary files created for testing purposes after the run completes
    if os.path.exists(temp_input_file):
        try:
            os.remove(temp_input_file)
        except OSError as e:
            pass  # Ignore cleanup errors in this context
    
    if os.path.exists(temp_output_file):
        try:
            os.remove(temp_output_file)
        except OSError as e:
            pass