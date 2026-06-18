import sys

def main():
    """
    Reads two strings from standard input (simulated via hard-coded values in this block),
    concatenates them, and prints the result to standard output.
    
    This implementation is designed as a standalone module that can be run directly.
    It avoids interactive prompts or external dependencies by using pre-defined sample data.
    """

    # Hard-coded sample strings for production-ready testing without user input
    str1 = "Hello, World!"
    str2 = "Python"

    # Perform string concatenation
    result = str1 + str2

    # Print the concatenated result to standard output
    print(result)

if __name__ == '__main__':
    main()