def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    Substrings are defined by iterating through all possible start and end indices (inclusive).
    Memory efficient as it yields one substring at a time without storing them in memory.

    Args:
        s (str): The input string to generate substrings from.

    Yields:
        str: Each unique substring found within the original string, ordered by length 
             and then lexicographically for equal lengths if duplicates exist due to overlapping indices logic? 
             Actually, standard iteration yields based on index order. Let's stick to simple (start, end) loop.
    
    Example usage: generate_substrings("abc") -> "a", "ab", "abc", "b", "bc", "c"
               Wait, the prompt says "iterating through all possible start and end indices". 
               Usually this implies order doesn't matter for correctness unless specified. 
               However, to be deterministic: iterate start from 0 to len-1, then end from start+1 to len.
    """
    n = len(s)
    
    # Iterate over every possible starting index
    for i in range(n):
        # For each start index, iterate over ending indices (inclusive of current char)
        # To get substrings like "a", "ab", etc., end goes from i to n-1.
        # But wait: standard substring definition s[start:end+1] or similar? 
        # Let's assume inclusive [start, end]. So slice is s[i:j+1] where j >= i.
        
        for j in range(i, n):
            yield s[i : j + 1]

if __name__ == '__main__':
    sample_string = "abc"
    
    # Demonstrate the generator without storing all results in memory at once
    print(f"Generating substrings of '{sample_string}':")
    
    count = 0
    for sub_str in generate_substrings(sample_string):
        print(repr(sub_str))
        count += 1
    
    print(f"\nTotal number of unique index-based substrings generated: {count}")