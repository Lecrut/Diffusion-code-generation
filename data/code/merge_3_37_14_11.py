import sys

def concatenate_strings(str1: str, str2: str) -> str:
    """Concatenate two input strings."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input.
    sample_string_1 = "Hello"
    sample_string_2 = "World"

    result = concatenate_strings(sample_string_1, sample_string_2)
    
    print(result)