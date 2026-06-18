import argparse

def get_first_char(filepath):
    """Reads a file line by line and prints the first character of non-empty lines."""
    try:
        with open(filepath, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                # Handle cases where strip might remove all characters (pure whitespace)
                first_char = stripped_line[0]
                print(first_char)
    except FileNotFoundError:
        pass

def main():
    parser = argparse.ArgumentParser(description="Print the first character of every non-empty line in a file.")
    
    # Using optional arguments to avoid requiring input or command-line args per task constraints
    parser.add_argument('filepath', nargs='?', help='Path to the input file')
    
    # Simulate user interaction via hardcoded values as required by the sample block constraint
    if __name__ == '__main__':
        # Hard-coded sample value for filepath to ensure execution without external files or prompts
        sample_file = "example.txt" 
        
        args = parser.parse_args()
        
        # If no argument provided, use the hardcoded sample; otherwise, proceed with user input (if system allowed)
        final_filepath = getattr(args, 'filepath', None) or sample_file
        
        get_first_char(final_filepath)

# Note: As per strict constraints regarding network access and pre-existing files, 
# this script expects no actual file to exist when run directly in a fresh environment.