import sys

def combine_strings(str1: str, str2: str) -> str:
    """Combines two strings by concatenating them."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    string_a = "Hello"
    string_b = "World"
    
    result = combine_strings(string_a, string_b)
    print(result)