import argparse

def main():
    parser = argparse.ArgumentParser(description="Prints the first character of every non-empty line in a file.")
    
    # Although the prompt forbids using required arguments, we include this to satisfy the 'argparse' usage requirement while keeping it optional.
    # If no path is provided via command line or sample value, it defaults to an empty string which will be handled gracefully below.
    parser.add_argument('file_path', nargs='?', help="Path to the file.")

    args = parser.parse_args()

    # Default sample behavior if no argument is passed and user input/interaction is forbidden
    if not args.file_path:
        sample_file = "sample_data.txt"
    
    try:
        with open(sample_file, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                # Check if the line is non-empty after stripping whitespace
                if len(stripped_line) > 0:
                    print(stripped_line[0])
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    main()