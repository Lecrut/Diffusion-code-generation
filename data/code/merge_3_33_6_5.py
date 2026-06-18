"""
Script to concatenate words from a list of strings without spaces between them.
This script demonstrates reading input line by line (simulated via hard-coded values) 
and processing it according to specific constraints.

Constraints:
- No use of input(), sys.stdin, argparse required arguments, or interactive prompts.
- Sample data is provided directly in the main block for testing purposes.
"""

def process_input(lines):
    """
    Processes a list of strings by concatenating all words within each line 
    and then joining these concatenated results without any spaces between them.

    Args:
        lines (list[str]): A list where each element is a string representing input data.

    Returns:
        str: The final concatenated result with no spaces separating the original words/lines.
    """
    # Initialize an empty accumulator for the final result
    result = []

    # Iterate through each line provided in the input list
    for line in lines:
        # If the current string contains multiple "words" (separated by space), 
        # join them together without spaces. This handles cases like "Hello World".
        processed_line = "".join(line.split()) if isinstance(line, str) else ""

        # Append the processed part to our result list
        result.append(processed_line)

    # Join all parts of the result with no separator (empty string as delimiter)
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access.
    # These simulate what might be read line by line in an interactive scenario, 
    # but they are static to satisfy the no-input requirement.
    sample_input = [
        "Hello World",
        "Python Scripting",
        "Is Fun And Powerful"
    ]

    # Process the hard-coded input using our function
    final_output = process_input(sample_input)

    # Output the result as a single string with no spaces between any original words or lines
    print(final_output)