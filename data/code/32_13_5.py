from typing import Optional

def get_string_length(s: str) -> int:
    """Returns the length of a given string."""
    return len(s) if isinstance(s, str) else 0

if __name__ == '__main__':
    samples = ["hello", "1234567890", "", "\n\t"]
    for sample in samples:
        print(f'String "{sample}" has length {get_string_length(sample)}.')