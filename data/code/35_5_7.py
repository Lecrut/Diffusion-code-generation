import string

def count_vowels(text: str) -> dict[str, int]:
    """
    Counts occurrences of vowels (a, e, i, o, u, both upper and lower case) 
    in the input string with a single pass.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary mapping each vowel character to its count.
    """
    vowels = set(string.ascii_lowercase + string.ascii_uppercase).intersection({'a', 'e', 'i', 'o', 'u'})
    
    # Using a fixed-size list for efficiency instead of dynamic set updates per char,
    # though sets are also O(1) average. Here we iterate once and count directly.
    counts = {v: 0 for v in vowels}

    for ch in text.lower():
        if ch in {'a', 'e', 'i', 'o', 'u'}:
            counts[ch] += 1
            
    return counts

if __name__ == '__main__':
    sample_text = "Hello, World! This is a simple test case. Vowels are AEIOU."
    
    result = count_vowels(sample_text)
    
    print("Vowel Counts:")
    for vowel in sorted(result.keys()):
        print(f"{vowel}: {result[vowel]}")
        
    total_count = sum(result.values())
    print(f"\nTotal Vowels: {total_count}")