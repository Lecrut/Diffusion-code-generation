import argparse

def main():
    parser = argparse.ArgumentParser(description="Prints the first character of every non-empty line in a file.")
    
    # Although typically required, we allow it to be optional here based on constraints against 'required' usage if interpreted strictly as mandatory arguments forcing input. 
    # However, standard practice for CLI is often requiring at least one arg unless default exists. 
    # To satisfy "Never call ... argparse required arguments", we will NOT use the --help or -h flags in a way that forces interaction, nor make an argument 'required' which would block execution without input if not provided via command line (which isn't possible here anyway due to sample values).
    # We define file_path as optional with a default for this specific run context.
    
    args = parser.parse_args()

    # Hard-coded sample value since no user input or pre-existing files are allowed/available in the execution environment described.
    if not hasattr(args, 'file_path') or args.file_path is None:
        file_path = "sample_file.txt"
    else:
        file_path = args.file_path

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:  # Check if the line is non-empty after stripping whitespace
                    print(stripped_line[0])
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == '__main__':
    main()