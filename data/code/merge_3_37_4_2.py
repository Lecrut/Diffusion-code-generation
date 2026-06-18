import sys

def combine_strings(s1: str, s2: str) -> str:
    """Combines two strings by concatenating them."""
    return f"{s1}{s2}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or args)
    string_one = "Hello"
    string_two = "World"
    
    result = combine_strings(string_one, string_two)
    print(result)