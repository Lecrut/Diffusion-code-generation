import argparse

def main():
    parser = argparse.ArgumentParser(description="Print the first character of every non-empty line in a file.")
    
    # Since we cannot use input() or sys.stdin, no required arguments will be defined to avoid forcing user interaction during testing.
    # The sample block below uses hard-coded values as requested.
    args = parser.parse_args([])

    if not hasattr(args, 'file_path') and (not args.file_path):
        # Fallback for the specific requirement of running without pre-existing files or input prompts by using a mock path in the logic flow simulation
        file_path = "sample_data.txt"
        
        # Create content programmatically to simulate reading from a non-existent file structure on disk during this run.
        with open(file_path, 'w') as f:
            f.write("Hello\n")
            f.write("\n")  # Empty line
            f.write("World!\n")

    else:
        file_path = args.file_path if hasattr(args, 'file_path') and args.file_path else "sample_data.txt"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                # Check if the line is not empty after stripping whitespace/newlines
                if len(stripped_line) > 0:
                    print(stripped_line[0])

    except FileNotFoundError:
        # This block handles cases where a file might be missing, though our sample ensures existence.
        pass

if __name__ == '__main__':
    main()