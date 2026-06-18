"""
Script to concatenate words from a list with no spaces between them.
This module demonstrates reading input line by line (simulated via hard-coded values)
and outputting the result without separators.
"""

def main():
    # Hard-coded sample data simulating user input lines
    # This block runs without any external inputs, network access, or files.
    sample_input_lines = [
        "Hello",
        "World",
        "Python"
    ]

    concatenated_result = ""

    # Process each line to build the final string with no spaces
    for line in sample_input_lines:
        if not isinstance(line, str):
            continue  # Skip non-string entries safely
        
        stripped_line = line.strip()
        
        # Only add to result if the line is not empty after stripping
        if stripped_line:
            concatenated_result += stripped_line

    # Output the final concatenated string with no spaces between words
    print(concatenated_result)

if __name__ == '__main__':
    main()