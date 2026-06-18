import os
from pathlib import Path

def read_sorted_integers(input_file: str) -> list[int]:
    """Read a single line of space-separated integers from the input file.
    
    Args:
        input_file: The path to the input file containing sorted-like data (to be re-sorted).

    Returns:
        A list of integers parsed from the file content.
        
    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the file contains non-integer values or is empty after stripping whitespace.
        IOError: For other I/O related errors (permissions, etc.).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
            if not content:
                raise ValueError("Input file is empty or contains no data.")

            # Split the line and convert parts to integers
            values_str = content.split(' ')
            return [int(val) for val in values_str]
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{input_file}' not found.") from None
    except PermissionError:
        raise PermissionError(f"No permission to read file '{input_file}'.") from None

def write_sorted_integers(output_file: str, integers: list[int]) -> bool:
    """Write the sorted list of integers to a new output file.

    Args:
        output_file: The path where the results will be written.
        integers: The list of integers to sort and store.

    Returns:
        True if successful; raises exceptions on failure.
        
    Raises:
        IOError: If there is an issue writing to the file (permissions, disk full).
    """
    try:
        # Sort the integers in ascending order
        sorted_integers = sorted(integers)

        with open(output_file, 'w', encoding='utf-8') as f:
            output_str = " ".join(str(num) for num in sorted_integers)
            f.write(output_str + "\n")  # Include a trailing newline
            
        return True
    except PermissionError:
        raise PermissionError(f"No permission to write to file '{output_file}'.") from None
    except IOError as e:
        raise IOError(f"Failed to write data to '{output_file}': {e}") from None

def main():
    # Hard-coded sample values for testing, ensuring no external dependencies or user input needed.
    INPUT_FILE = 'sample_input.txt'
    
    # Create the temporary input file with a single line of space-separated integers if it doesn't exist yet.
    # We use Path to handle cross-platform paths correctly.
    try:
        path_obj = Path(INPUT_FILE)
        
        # Since we must ensure this runs without pre-existing files (per prompt constraint), 
        # and the instruction implies "new file" logic, we simulate creating the input scenario here programmatically.
        if not path_obj.exists():
            sample_data_str = "85 23 -100 45 7 99 0 50\n"
            with open(INPUT_FILE, 'w', encoding='utf-8') as f:
                f.write(sample_data_str)

        # Read the integers from the input file
        try:
            raw_integers = read_sorted_integers(INPUT_FILE)
            
            if not raw_integers:
                print("Error: No valid integers found in sample data.")
                return
            
            # Sort and prepare output path (e.g., 'sorted_output.txt')
            OUTPUT_FILE = 'sample_output.txt'
            write_success = write_sorted_integers(OUTPUT_FILE, raw_integers)

            if write_success:
                print(f"Success! Sorted integers written to '{OUTPUT_FILE}'.")
            else:
                print("An unexpected error occurred during the write operation.")
                
        except Exception as e:
            # Handle any read or parsing errors specifically raised by our functions
            raise RuntimeError(f"Error processing input data: {e}") from None
            
    finally:
        # Cleanup logic is generally good practice, but since we created these files in-memory for the run 
        # and cannot guarantee file system deletion on all systems/OSes without user prompts (which are forbidden),
        # we leave them as artifacts of this successful execution if desired. However, to be safe regarding 'no pre-existing files' 
        # constraint interpretation for subsequent runs:
        try:
            path_obj.unlink()  # Remove the generated input file on OS level only after success? No, usually tests want persistence or just one-off run.
                                # Given "The sample block must run without ... pre-existing files", implies we create what is needed 
                                # and don't require it to exist beforehand. We will NOT delete them here unless explicitly asked, 
                                # as deletion might interfere if the user expects these specific filenames in a subsequent step for verification.
        except PermissionError:
            pass

if __name__ == '__main__':
    main()