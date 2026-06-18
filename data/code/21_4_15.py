import os

def read_and_sort_integers(input_path: str) -> list[int]:
    """Read a single line of space-separated integers from input file, sort them, 
    and return as a list."""
    try:
        with open(input_path, 'r') as f:
            content = f.read().strip()
        
        if not content:
            raise ValueError("Input file is empty or contains no data.")
            
        numbers = [int(x) for x in content.split()]
        return sorted(numbers)
    
    except FileNotFoundError:
        raise OSError(f"File '{input_path}' was not found.")
    except PermissionError:
        raise IOError(f"No permission to read file '{input_path}'.")
    except ValueError as e:
        raise ValueError(f"Invalid integer format in input data. {e}")

def write_sorted_integers(output_path: str, numbers: list[int]) -> None:
    """Write the sorted integers back to a new output file."""
    try:
        with open(output_path, 'w') as f:
            # Convert each number to string and join them into space-separated line
            f.write(' '.join(map(str, numbers)))
    
    except PermissionError:
        raise IOError(f"No permission to write to file '{output_path}'.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or pre-existing files.
    INPUT_FILE = 'input_data.txt'
    OUTPUT_FILE = 'sorted_output.txt'

    try:
        sorted_numbers = read_and_sort_integers(INPUT_FILE)
        write_sorted_integers(OUTPUT_FILE, sorted_numbers)
        print(f"Successfully processed {len(sorted_numbers)} integers.")
    except OSError as e:
        print(f"File system error occurred: {e}")
    except ValueError as e:
        print(f"Data validation error occurred: {e}")