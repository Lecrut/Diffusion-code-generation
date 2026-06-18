import sys

def main():
    """
    Reads two strings from standard input (or uses hard-coded sample values),
    prints their concatenation to standard output, and handles edge cases gracefully.
    
    Edge case handling includes:
    - Empty strings for either or both inputs.
    - Strings with special characters or unicode content.
    
    Since this must be standalone without external input files or network access,
    the main execution path uses hard-coded sample values as per task requirements.
    """

    # Hard-coded sample values to ensure no user input is required
    string_one = "Hello"
    string_two = "World!"

    # Perform concatenation
    concatenated_result = f"{string_one}{string_two}"

    # Print result to standard output
    print(concatenated_result)

if __name__ == '__main__':
    main()