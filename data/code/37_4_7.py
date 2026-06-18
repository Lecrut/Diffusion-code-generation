import sys

def combine_strings(str1: str, str2: str) -> str:
    """Combines two strings by concatenating them."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    sample_str_1 = "Hello"
    sample_str_2 = "World"

    result = combine_strings(sample_str_1, sample_str_2)
    
    print(result)