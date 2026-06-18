import sys

def concatenate_strings(str1: str, str2: str) -> str:
    """Concatenate two strings without modifying originals."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running 
    # without user input or command-line arguments.
    sample_input_1 = "Hello"
    sample_input_2 = ", World!"

    result = concatenate_strings(sample_input_1, sample_input_2)

    # Print the concatenated string to standard output.
    print(result)