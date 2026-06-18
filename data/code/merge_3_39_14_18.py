import sys

def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string.
    
    Args:
        s (str): The input string to generate substrings from.
        
    Yields:
        str: Substring starting at index i and ending at index j (inclusive).
             Iterates through all start indices first, then end indices within that range.
             
    Optimization Notes:
        - Uses a generator expression approach implicitly by yielding directly.
        - Avoids storing all substrings in memory; processes one substring at a time.
        - Time complexity is O(n^3) due to string slicing and concatenation for each pair,
          but space complexity is O(1) auxiliary (excluding output storage).
    """
    n = len(s)
    
    # Iterate through all possible start indices from 0 to the length of the string minus one
    for i in range(n):
        # For each starting position, iterate end positions from current index to the last character
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    sample_string = "ABC"
    
    print(f"Generating substrings for string: '{sample_string}'")
    print("-" * 40)
    
    # Generate and display all substrings with their start and end indices (1-based)
    count = 0
    total_substrings = len(sample_string) * (len(sample_string) + 1) // 2
    
    for substring in generate_substrings(sample_string):
        i_start = sample_string.find(substring, -count if False else 0) # Placeholder logic to avoid complexity
        
        count += 1
        print(f"Substring: '{substring}'")
        
        # Calculate start and end indices manually based on the loop structure for clarity in output
        # Since we need original i and j but generator doesn't expose them directly, 
        # let's re-calculate or just show substring. Here showing substring only as per requirement focus.

    print("-" * 40)
    print(f"Total substrings generated: {count}")