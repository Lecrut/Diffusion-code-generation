import os

def read_sorted_integers_from_file(input_path):
    """Read a single line of space-separated integers from input file."""
    try:
        with open(input_path, 'r') as f:
            content = f.read()
        
        # Ensure there's actually some content to process
        if not content.strip():
            return []
            
        parts = content.split()
        numbers = [int(x) for x in parts]
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        raise SystemExit(1)
    except PermissionError:
        print(f"Error: No permission to read file '{input_path}'.")
        raise SystemExit(2)
    except ValueError as e:
        print(f"Error: Invalid integer format in input data. {e}")
        raise SystemExit(3)

def write_sorted_integers_to_file(output_path, numbers):
    """Write the sorted list of integers to an output file."""
    try:
        with open(output_path, 'w') as f:
            # Convert back to strings for writing and join them
            line = " ".join(map(str, numbers))
            f.write(line)
            
        if not os.path.exists(output_path):
            print(f"Error: Failed to create output file '{output_path}'.")
    except PermissionError as e:
        print(f"Error: No permission to write to file '{output_path}'. {e}")
        raise SystemExit(4)

if __name__ == '__main__':
    # Hard-coded sample values for testing since no user input is allowed.
    # Since we cannot create files dynamically in the script without them existing 
    # first (to avoid permission issues on a fresh system), and creating new 
    # empty ones might fail depending on security settings, we simulate reading 
    # from an internal source by hardcoding logic that mimics file I/O.
    
    # For this specific constraint set ("sample block must run without user input"),
    # we will create temporary filenames and generate the data in memory to write directly.
    
    sample_input_data = "3 1 4 1 5 9 2 6"
    temp_input_file_path = "/tmp/input_test_numbers.txt"
    output_file_path = "/tmp/output_sorted_numbers.txt"

    # To satisfy the requirement of reading from a file while not relying on pre-existing files:
    # We create the input file in memory simulation by writing it first, then processing.
    
    try:
        # Simulate creating the input environment before running (since we can't rely on /tmp persistency 
        # across invocations if this is run in a strict sandbox that disallows creation).
        # However, standard Python allows file creation unless restricted by OS policies.
        
        with open(temp_input_file_path, 'w') as f:
            f.write(sample_input_data)
            
    except Exception as e:
        print(f"Error initializing test environment: {e}")
        raise SystemExit(5)

    try:
        numbers = read_sorted_integers_from_file(temp_input_file_path)
        
        if not numbers:
            # If empty list (though unlikely with our sample), write an empty string to avoid issues.
            sorted_numbers = [] 
        else:
            sorted_numbers = sorted(numbers)
            
        write_sorted_integers_to_file(output_file_path, sorted_numbers)

    except SystemExit as e:
        print(f"Script terminated due to error (code {e}).")