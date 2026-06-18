import string

def process_string(s: str) -> tuple[str, str, str]:
    """Returns a tuple of (original_str, lowercased_str, reversed_case_str)."""
    original = s
    lowercased = s.lower()
    
    # Create the swapped case version by iterating over characters and swapping their case.
    def swap_char(c: str) -> str:
        return c.swapcase() if not isinstance(c, str) else None
    
    reversed_case_chars = [c.swapcase() for c in original]
    reversed_case_str = ''.join(reversed_case_chars[::-1])
    
    return (original, lowercased, reversed_case_str)

if __name__ == '__main__':
    sample_input: str = "Hello World!"
    result_tuple: tuple[str, str, str] = process_string(sample_input)
    print(f"Original: {result_tuple[0]}")
    print(f"Lowercase: {result_tuple[1]}")
    print(f"Reversed Case: {result_tuple[2]}")