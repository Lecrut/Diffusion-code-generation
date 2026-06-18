def main():
    """
    Reads lines from a predefined sample input list (simulating user interaction)
    and concatenates all words into a single string with no spaces between them.
    
    Since direct interactive prompts, sys.stdin usage, or command-line arguments are prohibited,
    this function uses hard-coded sample values to demonstrate the logic without requiring external inputs.
    """

    # Hard-coded sample input lines (simulating user interaction)
    sample_input_lines = [
        "Hello",
        "World",
        "Python"
    ]

    # Initialize an empty string for concatenation
    result_string = ""

    # Iterate through each line in the sample input list
    for line in sample_input_lines:
        # Append characters from the current line to the result string directly,
        # ensuring no spaces are introduced between words or lines.
        result_string += line

    # Output the final concatenated result with no spaces
    print(result_string)

if __name__ == '__main__':
    main()