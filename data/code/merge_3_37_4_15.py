import sys

def combine_strings(s1: str, s2: str) -> str:
    """Combines two input strings."""
    return f"{s1}{s2}"

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user interaction or file I/O.
    string_a = "Hello"
    string_b = ", World!"

    result = combine_strings(string_a, string_b)
    
    print(result)