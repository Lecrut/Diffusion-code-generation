import os

def read_integers_from_file(file_path):
    """Reads a single line of space-separated integers from a file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            if not content:
                return []
            numbers = list(map(int, content.split()))
            return numbers
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise SystemExit(1)
    except PermissionError:
        print(f"Error: No permission to read file '{file_path}'.")
        raise SystemExit(2)
    except ValueError as ve:
        print(f"Error: Invalid integer format in the input line. {ve}")
        raise SystemExit(3)

def write_sorted_integers_to_file(file_path, numbers):
    """Writes a sorted list of integers to a file."""
    try:
        with open(file_path, 'w') as f:
            # Convert back to string and join by space
            output_string = ' '.join(map(str, numbers))
            f.write(output_string)
    except PermissionError:
        print(f"Error: No permission to write to file '{file_path}'.")
        raise SystemExit(2)
    except IOError as ie:
        print(f"Error: Failed to write to file '{file_path}'. {ie}")
        raise SystemExit(4)

def main():
    # Hard-coded sample input filename and output filename
    input_file = 'input_numbers.txt'
    output_file = 'sorted_output.txt'

    try:
        raw_integers = read_integers_from_file(input_file)
        sorted_integers = sorted(raw_integers)
        
        if not raw_integers:
            print("Input file was empty.")
            return
        
        write_sorted_integers_to_file(output_file, sorted_integers)
        print(f"Successfully wrote {len(sorted_integers)} integers to '{output_file}'.")

    except SystemExit as se:
        # Re-raise the system exit with specific code handled by caller or default behavior
        raise

if __name__ == '__main__':
    main()