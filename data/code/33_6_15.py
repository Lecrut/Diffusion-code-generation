import sys

def main():
    """
    Generates a concatenated string from hardcoded sample values.
    
    This script demonstrates reading input line by line (simulated via hard-coded data)
    and joining words without spaces between them, as requested in the functional description,
    while strictly adhering to constraints prohibiting interactive prompts or external inputs.
    """

    # Simulating user input with a list of strings representing lines
    sample_data = [
        "Python",
        "is",
        "awesome"
    ]

    result_lines = []

    for line in sample_data:
        if not line.strip():  # Skip empty lines to avoid adding extra newlines/characters blindly
            continue
        
        words = line.split()
        
        # Join each word with no spaces, then add the concatenated result of that line's words
        combined_line_wordless = ''.join(words)
        result_lines.append(combined_line_wordless)

    final_output = "".join(result_lines)

    print(final_output)

if __name__ == '__main__':
    main()