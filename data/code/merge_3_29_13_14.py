from typing import Callable

def reverse_string(s: str) -> str:
    return s[::-1] if isinstance(s, str) else ""

if __name__ == "__main__":
    sample_strings = ["hello", "world"]
    for val in sample_strings:
        print(f"Original: {val}, Reversed: {reverse_string(val)}")