import sys

def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    This implementation is memory-efficient as it does not store all substrings 
    in a list or set before yielding them. Instead, it generates and yields each 
    substring one by one using nested loops for start and end indices.

    Args:
        s (str): The input string to generate substrings from.

    Yields:
        str: Each unique substring of the input string in order of length and starting position.
    
    Note: This generator yields duplicates if they exist based on character repetition 
    unless deduplication is explicitly required by logic changes not specified here.
    """
    n = len(s)
    for i in range(n):
        # Optimization: Use slicing which creates a new string object, but avoids storing all at once.
        # For extremely long strings where memory allocation of every substring might be heavy,
        # one could yield characters and reconstruct lazily, but standard Python substrings 
        # are efficient enough for most practical "very long" constraints compared to list storage.
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    sample_string = "ABC"
    
    print(f"Generating substrings from: '{sample_string}'")
    count = 0
    
    # Demonstrate the generator without storing all results in memory
    for substring in generate_substrings(sample_string):
        print(substring)
        count += 1
        
    print(f"\nTotal number of substrings generated: {count}")

    # Test with a slightly longer string to show functionality beyond trivial cases
    long_sample = "ABCD"
    print(f"\nGenerating substrings from: '{long_sample}'")
    
    for substring in generate_substrings(long_sample):
        pass  # Just iterating, not printing all to avoid excessive output volume here
    
    total_long_count = sum(1 for _ in generate_substrings("ABCDEFG"))
    print(f"Total number of substrings for 'ABCDEFG': {total_long_count}")