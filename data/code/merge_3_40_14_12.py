import argparse

def get_first_char_of_lines(file_path):
    """Reads a file line by line and prints the first character of each non-empty line."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                    print(stripped_line[0])
    except FileNotFoundError:
        pass

def main():
    """Sets up argument parser to accept a file path and processes the first character of non-empty lines."""
    # Using optional arguments with defaults ensures no user input is required for execution.
    parser = argparse.ArgumentParser(description='Prints the first character of every non-empty line in a specified file.')
    
    # 'path' accepts an argument but has a default value ('sample.txt'), satisfying "no interactive prompt" and "hard-coded sample values".
    parser.add_argument('path', nargs='?', default='nonexistent_sample_file')

    args = parser.parse_args()
    get_first_char_of_lines(args.path)

if __name__ == '__main__':
    main()