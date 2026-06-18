import sys

def combine_strings(str1: str, str2: str) -> str:
    """Combines two input strings by concatenating them."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access is used here.
    str_a = "Hello"
    str_b = "World"

    result_str = combine_strings(str_a, str_b)
    
    print(result_str)