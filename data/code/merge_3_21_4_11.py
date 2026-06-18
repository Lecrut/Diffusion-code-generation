import os

def read_and_sort_file(input_path: str) -> list[int]:
    """Read a single line of space-separated integers from input_path, sort them, 
    and return as a list."""
    with open(input_path, 'r') as f:
        content = f.read().strip()

    try:
        raw_parts = [int(token) for token in content.split()]
    except ValueError:
        raise ValueError("Invalid integer format found. Ensure all tokens are valid integers.") from None
    
    return sorted(raw_parts)

def write_sorted_list(output_path: str, data: list[int]) -> None:
    """Write the sorted list of integers to output_path as a space-separated string."""
    with open(output_path, 'w') as f:
        f.write(' '.join(map(str, data)) + '\n')

def main() -> None:
    # Hard-coded sample input file path and content for demonstration. 
    # Since we cannot create files pre-existing in the environment during runtime execution without user action,
    # this script expects an existing file or raises an error if it doesn't exist as per robustness design,
    # but to satisfy "runnable" requirement with no setup dependency on external files:
    
    # We will simulate reading from a temporary internal state by generating the expected output directly? 
    # No, task says "reads a file". To ensure it runs without pre-existing files constraint violation, 
    # we must rely on standard behavior which fails if missing. However, to be truly runnable in a vacuum
    # where one might run this as-is and expect success immediately (as per sample block requirements),
    # let's create the input content dynamically within the logic before reading? No, that violates "reads a file".
    
    # Re-reading constraints: "The sample block must run without user input... or pre-existing files."
    # This implies we cannot assume `input_sample.txt` exists. 
    # The only way to satisfy this is if the script generates its own temporary input, reads it (simulating file), sorts, and writes output.
    # BUT standard "reads a file" semantics imply an external entity.
    
    # Let's interpret: Provide a sample block that attempts operation but handles creation of temp files internally 
    # to avoid dependency on user-prepared files, or simply creates the input string content in memory reads from?
    # Actually, creating a temporary file inside main() is allowed as it doesn't rely on "pre-existing" files from the OS.
    
    import tempfile
    
    input_path = 'temp_input_integers.txt'
    output_path = 'temp_output_sorted.txt'
    
    try:
        with open(input_path, 'w') as f:
            # Write sample data directly to avoid needing pre-existing file on disk
            f.write('5 2 8 1 9\n')

        sorted_numbers = read_and_sort_file(input_path)
        
        write_sorted_list(output_path, sorted_numbers)
    finally:
        # Clean up temporary files as they are generated during execution and not user-provided assets
        for path in [input_path, output_path]:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                pass

if __name__ == '__main__':
    main()