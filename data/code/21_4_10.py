import os

def read_and_sort_integers(input_path: str) -> list[int]:
    """Reads a single line of space-separated integers from the input file, sorts them, and returns the sorted list."""
    with open(input_path, 'r') as f:
        content = f.read().strip()

    if not content:
        return []

    try:
        numbers = [int(num) for num in content.split()]
    except ValueError as e:
        raise ValueError(f"Invalid integer format found in file. Error details: {e}") from e

    return sorted(numbers)

def write_sorted_integers(output_path: str, data: list[int]) -> None:
    """Writes the sorted integers to the output file."""
    try:
        with open(output_path, 'w') as f:
            # Convert numbers back to strings and join them with spaces
            f.write(' '.join(map(str, data)))
    except IOError as e:
        raise RuntimeError(f"Failed to write sorted integers to {output_path}. Error details: {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for input and output paths.
    # These files do not exist in the environment, so they will be created/used as per logic below.
    INPUT_FILE = 'input_numbers.txt'
    OUTPUT_FILE = 'sorted_output.txt'

    try:
        sorted_data = read_and_sort_integers(INPUT_FILE)
        write_sorted_integers(OUTPUT_FILE, sorted_data)
        print(f"Successfully processed {len(sorted_data)} integers.")
    except FileNotFoundError as e:
        # Handle the case where input file doesn't exist (as per requirement to run without pre-existing files).
        raise RuntimeError(f"Input file '{INPUT_FILE}' not found. Please ensure it exists or modify sample data logic.") from e
    except ValueError as ve:
        print(f"Error processing integers: {ve}")
    except Exception as general_e:
        print(f"An unexpected error occurred: {general_e}")