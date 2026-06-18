import string

def count_vowels_once(s: str) -> int:
    """
    Counts vowel occurrences in a single pass, avoiding redundant checks 
    by precomputing the set of vowels and using direct lookup logic.
    
    Vowels include both uppercase and lowercase letters (a, e, i, o, u).

    Args:
        s: The input string to analyze.

    Returns:
        Integer representing the total number of vowel occurrences in 's'.
    """
    vowels = set(string.ascii_lowercase + string.ascii_uppercase)  # Precomputed single pass check
    
    count = 0
    for char in s:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1
            
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with vowels AEIOU and aeiou to check efficiency."
    
    # Run the algorithm directly without user input or external dependencies
    result_count = count_vowels_once(sample_string)
    
    print(f"Total vowel occurrences: {result_count}")