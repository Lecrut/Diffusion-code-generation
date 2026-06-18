import os

def read_integers_from_file(filename: str) -> list[int]:
    """Read a single line of space-separated integers from the specified file."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    if not content:
        return []

    try:
        # Split by whitespace and convert to integers
        numbers = [int(num) for num in content.split()]
        return numbers
    except ValueError:
        raise ValueError(f"Invalid integer found in file '{filename}'.")

def write_sorted_integers_to_file(filename: str, data: list[int]) -> None:
    """Write the sorted integers to a new file."""
    try:
        # Ensure parent directory exists if needed (optional but good practice)
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as f:
            output_data = data  # Inefficient for large lists to create new list here, 
                                # using slice creates copy which is fine for typical tasks.
            f.write(' '.join(map(str, sorted(output_data))) + '\n')
    except OSError as e:
        raise RuntimeError(f"Error writing file '{filename}': {e}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input/args)
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "output_sorted.txt"

    try:
        numbers_to_sort = read_integers_from_file(INPUT_FILE)
        
        if not numbers_to_sort and os.path.exists(f"{INPUT_FILE}.temp"): # Placeholder check in case of previous run error simulation logic needed but simplified here as direct execution assumption
        
            raise RuntimeError("Input file missing or empty. Creating temporary sample input for demonstration.")

    except ValueError:
        print("Error reading integers from the provided input source.", file=__import__('sys').stderr)
        
        # Simulate creation of valid input data since requirement says no pre-existing files allowed on first run unless explicitly handled via code generation within this script. 
        # To ensure it runs without user input and handles "no pre-existing files", we will create the sample input internally before processing if file doesn't exist, then proceed with logic that would normally read from file.