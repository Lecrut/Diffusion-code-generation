import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Prints the first character of every non-empty line from a file."
    )
    
    # Note: As per instructions, we will not use required arguments or interactive prompts like input().
    # We will simulate user interaction via command-line flags for testing purposes.
    parser.add_argument(
        "file_path",
        help="The path to the text file to process."
    )

    args = parser.parse_args()

def get_first_char_of_non_empty_line(file_path):
    """
    Reads a file line by line and prints the first character of each non-empty line.
    
    Args:
        file_path (str): Path to the input file.
        
    Returns:
        None
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an issue reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:  # Check if line is not empty or whitespace only
                    first_char = stripped_line[0]
                    print(first_char)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")

if __name__ == '__main__':
    # Hard-coded sample values to simulate user input without requiring actual files or network access.
    # This block runs independently and demonstrates the script's functionality using a temporary string as if it were a file content.
    
    # Since we cannot create real files in this isolated environment for guaranteed success,
    # we will use argparse with default values (if supported by version) OR simulate the logic directly 
    # to ensure no pre-existing files are needed and no input() calls occur outside of argparse parsing simulation.
    
    # To strictly adhere to "no required arguments" and "hard-coded sample", let's set a dummy file path 
    # that points to an empty string buffer if possible, but standard open requires real paths.
    # Instead, we will use the --help flag logic implicitly by providing defaults in argparse or simply mocking via sys.argv simulation?
    
    # Re-reading constraints: "Never call input(), sys.stdin...". 
    # We can set default values for arguments if available (Python 3.7+ supports -d/--default).
    # However, to be safe and cross-version compatible while avoiding required args logic errors on missing files:
    
    try:
        import argparse
        
        parser = argparse.ArgumentParser()
        
        # Using --help is not allowed as it expects flags but we can set defaults.
        # Let's define a default file path that doesn't exist, then handle the error gracefully 
        # OR better yet, use a trick where we pass an empty string or simulate via sys.argv if allowed? 
        # Constraint says: "Do not include markdown fences...". It implies standard script execution.
        
        # Best approach for 'hard-coded sample' without real files:
        # We will configure the parser to accept any path, but then immediately override it with a mock content generator 
        # OR we assume the user wants to see how it works on a non-existent file? No, that prints nothing.
        
        # Let's create a temporary directory and file in memory-like fashion by writing to disk temporarily?
        # Constraint: "without... pre-existing files". Creating one might be borderline but necessary for reading.
        # BUT the constraint also says "The sample block must run without... pre-existing files." 
        # This usually means no external dependencies or network, not necessarily forbidding creating temp files in current dir?
        # However, to keep it pure and safe: We will simulate the file content by printing directly if we can't read a real one.
        
        # Actually, let's use argparse with default values for arguments that don't require user input at runtime 
        # (i.e., defaults are set). But 'file_path' is positional. Positional args usually have no default in strict CLI unless handled carefully.
        
        # Alternative interpretation: The script should work if run without arguments, using the hard-coded value internally?
        # argparse doesn't support positional defaults easily without custom logic or specific versions.
        
        # Let's use a workaround with sys.argv simulation inside the main block to satisfy "hard-coded sample values" 
        # while avoiding 'input()' and ensuring no network access. We set up args manually before parsing? No, that bypasses argparse structure slightly but is valid Python.
        
        # Better: Use --help or just parse normally and assume an empty file path results in error handling which prints nothing (correct behavior). 
        # But the task implies showing output ("prints..."). So we need data.
        
        # Final Plan: Create a temporary file with sample text, read it, close temp file immediately after processing? 
        # This satisfies "no pre-existing files" if created on-the-fly in current directory (which is allowed unless specified otherwise).
        # Actually, simplest compliant way that guarantees output without real network/files dependency logic complexity:
        
        # We will use a string buffer approach by passing an empty list simulation via argparse defaults? 
        # No, let's just create the file on disk temporarily. It's standard CLI behavior to handle files.
        
        import tempfile
        
        sample_text = "Hello\nWorld\nPython"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
            tmp_file.write(sample_text)
            temp_path = tmp_file.name
            
        try:
            get_first_char_of_non_empty_line(temp_path)
        finally:
            # Clean up the temporary file to ensure no pre-existing files remain and maintain cleanliness.
            import os
            if os.path.exists(temp_path):
                os.remove(temp_path)

    except Exception as e:
        print(f"Error during sample execution: {e}")