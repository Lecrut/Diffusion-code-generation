import os

def read_and_sort_integers(file_path: str) -> list[int]:
    """Reads a single line of space-separated integers from a file, sorts them, 
    and returns the sorted list."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified input file '{file_path}' does not exist.")

    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            # Handle empty files or lines without integers gracefully by returning an empty list
            if not content:
                return []
                
            parts = content.split()
            numbers = [int(x) for x in parts]
    except ValueError:
        raise ValueError("Input file contains non-integer values.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read the specified input file '{file_path}'.")

    return sorted(numbers)

def write_sorted_integers(file_name: str, numbers: list[int]) -> None:
    """Writes a space-separated string of integers to a new file."""
    if not os.path.exists(os.path.dirname(file_name)):
        # Attempt to create the directory structure if it doesn't exist (optional robustness)
        try:
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
        except PermissionError as e:
            raise PermissionError(f"Permission denied to write or access directories for file '{file_name}'.") from e

    output_path = f"{file_name}.sorted.txt"  # Conventionally append '.sorted' suffix unless specified otherwise, 
                                              # but here we strictly follow the task's "new file" requirement.
                                              # To avoid ambiguity on exact filename extension not requested:
                                              # We will use a fixed name for reproducibility as per sample requirements.

    try:
        with open(output_path, 'w') as f:
            if numbers:
                sorted_str = ' '.join(map(str, numbers))
                f.write(sorted_str + '\n')
            else:
                # If the input was empty or had no integers, write an empty line to indicate success/structure
                pass 
    except PermissionError as e:
        raise PermissionError(f"Permission denied to write to file '{output_path}'.") from e

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or pre-existing files.
    # We create a temporary input file in memory logic by reading directly, 
    # but since the task requires "reads a file", we simulate the existence of an input file 
    # by creating one dynamically before execution to satisfy the "no pre-existing files" constraint 
    # while ensuring the script runs standalone.
    
    import tempfile
    
    sample_data = [50, 12, -3, 87, 4]

    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_input_file:
            input_path = tmp_input_file.name
            # Write the single line of space-separated integers to the temp file
            sample_data_str = ' '.join(map(str, sample_data))
            tmp_input_file.write(sample_data_str + '\n')

        try:
            sorted_list = read_and_sort_integers(input_path)
            
            output_name = "sorted_output.txt" # Fixed name for deterministic behavior in this script context
            
            write_sorted_integers(output_name, sorted_list)
            
            print(f"Sorted integers written to {output_name}")
            print("Content:", ' '.join(map(str, sorted_list)))
        finally:
            # Clean up the temporary input file immediately after use to ensure no persistent files remain
            os.unlink(input_path)

    except FileNotFoundError as e:
        print(f"Error (File Not Found): {e}")
    except ValueError as e:
        print(f"Error (Invalid Input Data): {e}")
    except PermissionError as e:
        print(f"Error (Permission Denied): {e}")