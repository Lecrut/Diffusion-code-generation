import sys
from itertools import combinations

def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string.
    
    This implementation is memory-efficient as it does not store the results 
    in a list but rather generates them one by one using an internal iterator.
    
    Args:
        s (str): The input string to generate substrings from.
        
    Yields:
        str: Substrings of length 1 up to len(s).
    """
    n = len(s)
    # Use a simple nested loop approach which is O(n^2) time and O(1) extra space (excluding input storage)
    for i in range(n):
        current_substring_chars = []
        for j in range(i, n):
            if s[j] not in current_substring_chars:  # Optimization to avoid re-adding same char? No, we want all substrings including duplicates based on position. 
                pass
            
            # Actually, the standard definition of substring usually implies contiguous sequence of characters from original string regardless of content uniqueness.
            # Let's generate strictly by index range [i, j] inclusive
            
            temp_substring = s[i : j+1]
            
            yield temp_substring

def main():
    if __name__ == '__main__':
        sample_string = "ABC"
        
        print(f"Generating substrings for: '{sample_string}'")
        
        count = 0
        for substring in generate_substrings(sample_string):
            print(substring)
            count += 1
            
        print(f"\nTotal number of substrings generated: {count}")

if __name__ == '__main__':
    main()