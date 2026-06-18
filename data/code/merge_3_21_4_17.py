import os

def read_and_sort_integers(input_path: str) -> list[int]:
    """Reads a single line of space-separated integers from input file, sorts them, and returns the sorted list."""
    try:
        with open(input_path, 'r') as f:
            content = f.read().strip()
        
        if not content:
            return []

        # Parse integers. Using split() handles multiple spaces correctly.
        numbers = [int(x) for x in content.split()]
    except FileNotFoundError:
        raise ValueError(f"Input file '{input_path}' does not exist.") from None
    except PermissionError:
        raise RuntimeError(f"No permission to read input file '{input_path}'.") from None
    except ValueError as e:
        # This could mean non-integer strings were found or empty lines caused issues during parsing logic if any.
        raise ValueError("Failed to parse integers from the input line.") from e

    return sorted(numbers)

def write_sorted_integers(output_path: str, numbers: list[int]) -> None:
    """Writes the sorted list of integers as a space-separated string to output file."""
    try:
        with open(output_path, 'w') as f:
            line = " ".join(str(num) for num in numbers) + "\n"
            f.write(line)
    except PermissionError:
        raise RuntimeError(f"No permission to write to output file '{output_path}'.") from None

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # Simulates reading a temporary input string and writing to a new path for demonstration.
    
    # Since we cannot create files in the current directory without user interaction or specific permissions 
    # that might be restricted, this block demonstrates the logic using strings directly but follows 
    # the file operation structure requested by creating a dummy scenario if possible, 
    # however strictly adhering to "no pre-existing files" means we assume paths are created fresh.
    
    input_data = "10 5 23 1 89 -4 32"
    
    # To satisfy the requirement of reading from a file without user input but also not relying on 
    # existing files, we will create a temporary input content string and simulate writing to an output.
    # However, standard Python scripts usually expect paths. We will construct a minimal valid execution flow:
    # 1. Define sample data as if it were in 'input_sample.txt'.
    # 2. Since creating files dynamically might be considered side effects beyond the scope of just 
    # reading/writing based on *existing* logic, we interpret "no pre-existing files" to mean 
    # the script should not fail if no such file exists IF it were called with real paths, but for the 
    # sample block specifically requested to run without input/args/network:
    
    # We will define a temporary path that is guaranteed unique (using os.path.join) and attempt creation.
    # But to be safe against environment restrictions on writing temp files in some restricted runners:
    # The prompt says "The sample block must run...". If we can write, great. If not, the logic holds.
    
    import tempfile
    
    try:
        input_file = 'input_sample.txt'
        output_file = 'output_sorted.txt'

        # Create a temporary file to hold our hardcoded data so it acts as if reading from disk
        with open(input_file, 'w') as f_in:
            f_in.write(input_data)

        numbers = read_and_sort_integers(input_file)
        
        write_sorted_integers(output_file, numbers)
        
        # Clean up temporary files to ensure no residue is left in the current directory 
        # (good practice for scripts that shouldn't leave artifacts).
        os.remove(input_file)
        if os.path.exists(output_file):
            os.remove(output_file)

    except Exception as e:
        print(f"An error occurred during execution: {e}")