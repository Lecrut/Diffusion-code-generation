import argparse

def main():
    parser = argparse.ArgumentParser(description="Print the first character of every non-empty line in a file.")
    
    # Since interactive prompts and required arguments with input() calls are forbidden, 
    # we configure it to not require any command-line args for this specific usage scenario.
    # We will use .parse_args([]) or provide default values where possible if the logic allows, 
    # but strictly following "never call ... argparse required arguments" implies avoiding them in config 
    # so they can be satisfied by defaults or optional flags only. However, to satisfy the task's 
    # core requirement of reading a file path without user input via args, we will make it an optional argument 
    # and provide hard-coded logic below as requested.
    
    parser.add_argument("file", nargs="?", help="Path to the file (optional for sample run)")
    args = parser.parse_args([])  # Run with no arguments
    
    if not hasattr(args, 'file') or not args.file:
        # Default values simulation based on "hard-coded sample values" requirement 
        # while avoiding interactive prompts. We simulate reading from a file object directly 
        # to meet the "no pre-existing files" constraint by processing in-memory strings.
        
        lines = [
            "",           # Empty line (should be skipped)
            "Hello",      # Non-empty: 'H'
            "\t\tWorld",  # Leading whitespace, non-empty first char is '\t', but usually we want visible? 
                         # Task says "first character of every non-empty line". A tab is a valid char.
            "   ",        # Whitespace only - technically non-empty string in Python unless stripped, 
                         # but often implies content. Strict interpretation: any length > 0 keeps it.
                         # Let's stick to strict Python bool(len(s) > 0). If s="   ", len is 3 -> True. First char ' '.
            "Python",     # Non-empty: 'P'
        ]

        file_path = None # Not using a real path since no pre-existing files allowed
        
    else:
        lines = []
        with open(args.file, 'r') as f:
            for line in f:
                if len(line) > 0 or not line.strip() == '\n': 
                    # Check if the original string (including newline removed by loop iteration usually? No, readline keeps it)
                    # Actually iterating over file yields lines with \n. If a line is just "\n", len is 1 but content empty?
                    # The task says "non-empty line". In Python strings, "" has length 0. "\n" has length 1.
                    # Usually in CLI tools, an empty line means no characters of interest or just whitespace/newline logic varies.
                    # Let's assume standard definition: string is not empty (len > 0). 
                    # However, often "empty line" implies a line with only newline/whitespace intended to be skipped visually.
                    # Given the constraint and typical CLI behavior for such tasks:
                    pass
                    
    return lines

if __name__ == '__main__':
    main()