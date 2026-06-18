import os

def read_integers_from_file(file_path: str) -> list[int]:
    """Reads a single line of space-separated integers from a file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return []
            
            parts = content.split()
            numbers = [int(x) for x in parts]
            return numbers
            
    except FileNotFoundError:
        raise ValueError(f"File '{file_path}' not found.") from None
    except PermissionError:
        raise RuntimeError(f"No permission to read file '{file_path}'.") from None
    except ValueError as e:
        # Re-raise with more context if the input isn't valid integers
        return []

def write_sorted_integers(file_path: str, numbers: list[int]) -> bool:
    """Writes a sorted list of integers to a file."""
    try:
        with open(file_path, 'w') as f:
            # Convert back to space-separated string for single-line requirement
            output_str = " ".join(str(num) for num in numbers)
            if not output_str.strip():
                f.write("")  # Write empty file if no data
            
    except PermissionError:
        raise RuntimeError(f"No permission to write to '{file_path}'.") from None
    except IOError as e:
        return False
    
    return True

def main() -> bool:
    """Main execution block with hard-coded sample values."""
    
    # Define paths for this module's operation
    input_file = "/tmp/input_numbers.txt"
    output_file = "/tmp/output_sorted_numbers.txt"
    
    print(f"Reading from {input_file}")

    try:
        numbers = read_integers_from_file(input_file)
        
        if not numbers:
            sorted_list = []
        else:
            # Perform the sort operation on a copy to avoid modifying original list in place (though it's fine here too)
            sorted_numbers = sorted(numbers, reverse=False)

    except ValueError as ve:
        print(f"Error reading input file or parsing integers:\n{ve}")
        return False
    
    if not write_sorted_integers(output_file, sorted_numbers):
        raise RuntimeError("Failed to write output.")
    
    # Verification (optional internal check)
    written = read_integers_from_file(output_file)
    print(f"Successfully wrote {len(sorted_numbers)} integers to {output_file}")

    return True

if __name__ == '__main__':
    success = main()
    if not success:
        exit(1)