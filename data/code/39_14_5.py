import sys

def generate_substrings(s: str) -> iter[str]:
    """
    Generator that yields all possible substrings of a given string 's'.
    
    This function uses an efficient approach by iterating through every character as the starting point,
    and then extending the substring from that start until the end of the string.
    
    Args:
        s (str): The input string to generate substrings from.
        
    Yields:
        str: Substrings starting at each index up to length 's'.
    """
    n = len(s)
    # Outer loop iterates through every possible start index
    for i in range(n):
        # Inner logic starts a new substring with s[i] and builds it character by character.
        # This avoids creating the full set of all substrings first, keeping memory usage low (O(1) auxiliary per yield).
        current_substring = ""
        for j in range(i, n):
            if len(s) > 0:
                char_to_add = s[j]
                current_substring += char_to_add
                # Yield the newly formed substring at each step to avoid storing them all in memory.
                yield current_substring

if __name__ == '__main__':
    sample_string = "HELLO"
    
    print(f"All substrings of '{sample_string}':")
    
    for sub in generate_substrings(sample_string):
        # Sorting the output makes it easier to verify correctness, though not required.
        sorted_chars = ''.join(sorted(sub)) 
        if len(set(sub)) != 1:
            print(sub)
        
print(f"Example count verification (lengths of substrings generated for '{sample_string}'):")
    
    # Count how many times each unique substring length appears to demonstrate functionality without printing all