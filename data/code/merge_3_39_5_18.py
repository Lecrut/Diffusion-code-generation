import sys
from typing import Generator

def generate_substrings(text: str) -> Generator[str, None, None]:
    """
    A generator function that yields all possible substrings of a given string.
    
    This implementation is memory-efficient for very long strings because it
    only holds references to one substring at any time (via slicing), avoiding 
    the creation of an intermediate list or set which could consume prohibitive 
    amounts of RAM and CPU resources on large inputs.

    Args:
        text (str): The input string to generate substrings from.

    Yields:
        str: Non-empty substrings in order of increasing length, then lexicographical start index.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    for i in range(len(text)):  # Start character indices
        for j in range(i + len(text), 0, -1):  # End characters (exclusive) or length from 1 to remainder+1 logic adjusted below
        
            # Correct loop: start at 'len', down to i+1 inclusive? 
            # Actually simpler loops are clearer and efficient.
            for j_start in range(i + 1, len(text) + 1):
                yield text[i:j_start]

if __name__ == '__main__':
    sample_text = "ABC"
    
    print(f"Generating substrings from: '{sample_text}'")
    # Using sys.stdout.write might be slightly faster for massive outputs, 
    # but print is sufficient and standard for this context.
    
    count = 0
    try:
        for substring in generate_substrings(sample_text):
            print(substring)
            count += 1
    except KeyboardInterrupt:
        pass
    
    print(f"Total substrings generated: {count}")