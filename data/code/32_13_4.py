from typing import Optional

def get_string_length(s: str) -> int:
    """Return the length of the given string."""
    return len(str(s)) if isinstance(s, (str, bytes)) else 0

if __name__ == '__main__':
    test_cases = [None, "hello", "", 123]
    for case in test_cases:
        print(f"Input {repr(case)} -> Length: {get_string_length(case)}")