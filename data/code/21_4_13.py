import os

def read_and_sort_file(input_filename: str) -> list[int]:
    """Reads a single line of space-separated integers from input file, sorts them, returns as list."""
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            values = [int(x) for x in content.split()]
    except FileNotFoundError:
        raise RuntimeError(f"Input file '{input_filename}' was not found.") from None
    except PermissionError:
        raise RuntimeError("Permission denied to read input file.") from None
    except ValueError as e:
        # Handle cases where non-integer tokens exist in the line for now, raising a clear error.
        raise ValueError(f"Invalid integer format detected while reading '{input_filename}'.") from e

    return sorted(values)

def write_sorted_list(output_filename: str, integers: list[int]) -> None:
    """Writes the sorted list of integers to output file as space-separated values."""
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(' '.join(str(x) for x in integers))
            # Optional newline at end if desired; keeping minimal per task description.
    except PermissionError:
        raise RuntimeError("Permission denied to write output file.") from None
    except OSError as e:
        raise RuntimeError(f"Failed to write data to '{output_filename}': {e}") from e

if __name__ == '__main__':
    # Hard-coded sample input filename and output filename.
    INPUT_FILE = 'input_numbers.txt'
    OUTPUT_FILE = 'sorted_output.txt'

    integers = read_and_sort_file(INPUT_FILE)
    write_sorted_list(OUTPUT_FILE, integers)