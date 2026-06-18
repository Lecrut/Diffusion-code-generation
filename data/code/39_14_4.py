import sys

def generate_substrings(s: str):
    """
    Generator that yields all possible substrings of a given string s.
    
    Substrings are defined by iterating through all valid start and end indices,
    ensuring the slice is non-empty (start <= end).
    
    Args:
        s (str): The input string to generate substrings from.
        
    Yields:
        str: A substring starting at index 'i' and ending before index 'j'.
       
    Optimizations:
        - Avoids creating a list of all substrings; yields one at a time.
        - Uses slice notation directly, which is efficient in Python for strings (which are immutable).
    """
    n = len(s)
    
    # Iterate start index from 0 to the last character inclusive
    for i in range(n):
        # Iterate end index from current start + 1 to length of string
        # This ensures substrings have at least one character.
        # Using slice s[i:j] where j goes up to n (inclusive) captures indices correctly.
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    sample_string = "hello"

    print(f"All substrings of '{sample_string}':")
    
    # Consume the generator to demonstrate functionality without storing results in memory
    for sub_str in generate_substrings(sample_string):
        print(repr(sub_str))