import argparse

def parse_arguments():
    """Parse command line arguments using argparse."""
    
    parser = argparse.ArgumentParser(
        description="Print the first character of every non-empty line in a file."
    )
    
    parser.add_argument("file_path", help="The path to the input file.")
    
    return parser.parse_args()

def get_first_characters(file_path):
    """Read the specified file and print the first character of each non-empty line."""
    
    with open(file_path, "r") as f:
        for line in f:
            stripped_line = line.strip()
            
            # Only process lines that are not empty after stripping whitespace
            if stripped_line:
                # Get only the very first character
                print(stripped_line[0])

def main():
    """Main execution block with hard-coded sample values."""

    
    args = parse_arguments()
    

    file_path = "input.txt"
    
    
    get_first_characters(file_path)

if __name__ == '__main__':
    pass
