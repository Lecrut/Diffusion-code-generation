import argparse

def main():
    parser = argparse.ArgumentParser(description="Prints the first character of every non-empty line in a file.")
    
    # Use an optional argument with a default value to avoid requiring user input or pre-existing files
    args = parser.parse_args()
    
    if not hasattr(args, 'file') and len(sys.argv) == 1:
        # Fallback for the sample block scenario where no arguments are provided at all (though argparse usually exits without defaults on optional file arg unless default is set)
        # To strictly follow "no user input", we will simulate a run using a hard-coded path in the if __name__ block logic below.
        pass

    # Since 'file' is not required, parser.parse_args() works with no arguments or with -h/--help
    # However, to make it runnable as requested without pre-existing files on disk for this specific sample run:
    import sys
    
    if len(sys.argv) == 1:
        # Simulate a file path argument using the default behavior of argparse (it won't exist yet in real execution context 
        # but here we force a scenario). Actually, to ensure "no user input", let's set up the sample block directly.
        pass

    # Re-reading requirements carefully: "Include an if __name__ == '__main__': block with hard-coded sample values."
    # This implies the script should be able to run standalone without needing actual files on disk during that specific execution,
    # OR it expects a file argument but the sample just sets one up. The constraint says "without ... pre-existing files".
    # Therefore, we cannot rely on `args.file` pointing to an existing real file in the interactive/sample environment unless we write/create it or simulate reading from stdin (which is forbidden).
    
    # Strategy: Set a default argument for 'file'. If no arg is passed and this isn't the sample block running? 
    # Actually, the instruction says "Include ... with hard-coded sample values". This usually means mocking inputs.
    # But `argparse` doesn't easily mock file paths without actually reading them unless we catch FileNotFoundError or use a dummy path that gets handled gracefully?
    
    # Correction: The task asks to read the file line by line. If no real file exists and we can't create one (no network/filesystem permissions guarantee), 
    # how do we satisfy "without pre-existing files"? 
    # We must assume the sample block will trigger a specific path that either doesn't exist but is handled, OR more likely, the user expects us to use `--file` with a value.
    
    # Let's set up argparse such that 'file' has a default of None or empty string? No, let's just parse normally and handle the case in main where 
    # we might need a fallback for demonstration if no args are passed AND file doesn't exist? 
    # Wait, "without ... pre-existing files". This likely means I should not assume `data.txt` exists.
    
    # Best approach: Define default_file = None or similar? No. Let's just let argparse handle the arguments normally but ensure the sample block sets a path that is handled gracefully if it doesn't exist (e.g., by printing an error message instead of crashing, OR using a string input to simulate).
    
    # Actually, looking at "hard-coded sample values", perhaps I should pass `-f` or `--file` with a value in the main block logic? No, that's still args.
    
    # Let's re-read: "Include an if __name__ == '__main__': block with hard-coded sample values." 
    # This suggests inside the `if __name__` block, we can set variables directly to simulate input without using argparse interaction or stdin.
    # But argparse is still being used for parsing? Or does it mean I should just use argparse normally but handle missing files gracefully in a way that doesn't crash if no file exists yet? 
    # The constraint "without ... pre-existing files" implies the script shouldn't fail trying to open `nonexistent.txt`.
    
    # Let's set up the code structure first.

def process_file(path):
    """Reads file and prints first char of non-empty lines."""
    with open(path, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                print(stripped_line[0])

if __name__ == '__main__':
    import sys
    
    # Setup argparse specifically to handle the requirement of not needing user input 
    # by setting a default or handling missing args gracefully in the sample context.
    
    parser = argparse.ArgumentParser(description="Process file lines.")
    parser.add_argument('--file', '-f', help='Path to the file')
    
    # If no arguments are provided and it's meant to be run without pre-existing files, 
    # we can simulate a scenario by checking sys.argv. However, to keep it clean:
    args = parser.parse_args()
    
    # Check if 'file' argument is missing; in the sample block context where "no pre-existing files" exist,
    # we might want to demonstrate behavior or skip? 
    # The prompt says "hard-coded sample values". This implies I should probably set a dummy path that doesn't need to physically exist on disk for this specific run if possible?
    # But open() will fail. Unless... the user expects me to create it? No, "without pre-existing files" usually means don't assume they are there.
    
    # Alternative interpretation: The sample values refer to command-line arguments passed directly in the script logic 
    # without asking the user (which is forbidden) or stdin. So I will set args.file manually for the demo run?
    # No, that bypasses argparse usage. But I can use `sys.argv` modification before parse_args? That's a trick but valid Python.
    
    if len(sys.argv) == 1:
        sys.argv = ['script', '-f', 'sample_data']

    args = parser.parse_args()

    file_path = getattr(args, 'file') or None
    
    # Since we cannot guarantee a file exists without network/filesystem access (which is forbidden), 
    # and the constraint says "without pre-existing files", I will modify the logic to handle non-existence gracefully
    # OR use a string that represents the sample value but doesn't try to open it if not present? 
    # Actually, if I set sys.argv = ['script', '-f', 'sample_data'], then argparse sees `-f`. 
    # The script will attempt `open('sample_data')`. If this file does NOT exist on the user's machine (which satisfies "no pre-existing files"), it crashes.
    
    # To satisfy "without ... pre-existing files" and avoid crash, I must ensure the path used in the sample block either:
    # 1. Creates a temp file? No, that might require permissions.
    # 2. Uses `sys.stdin`? Forbidden.
    # 3. Just prints an error message instead of crashing if file missing? That's good practice but not "printing first char".
    
    # Let's assume the instruction implies: Do NOT wait for user input to type a filename, and do NOT assume any specific file is already there on disk 
    # (so don't hardcode `open('data.txt')` without checking). Use argparse with an optional argument. 
    # For the sample block execution specifically ("hard-coded sample values"), I will simulate passing `-f` to argparse via sys.argv,
    # but since no file exists, I should probably catch FileNotFoundError or just let it fail? No, "runnable" usually implies success or graceful handling.
    
    # Let's try a different angle: Use `io.StringIO` in the sample block logic if args.file is missing/invalid? 
    # That simulates reading from a file without needing a real one!
    import io
    
    def get_input_stream(path):
        """Returns a stream. If path doesn't exist, returns StringIO with dummy content."""
        try:
            return open(path)
        except FileNotFoundError:
            # Simulate sample data since no pre-existing files are allowed/assumed
            print("File not found (simulating via StringIO for demo)...")
            stream = io.StringIO("\nHello\nWorld\tTest\n   \nEnd.")
            return stream
    
    if file_path and os.path.exists(file_path):
        f_in = open(file_path, 'r')
    else:
        # Simulate reading from a non-existent path as per "sample values" requirement 
        # without requiring the actual file to exist.
        dummy_data = "\nHello\nWorld\tTest\n   \nEnd."
        f_in = io.StringIO(dummy_data)