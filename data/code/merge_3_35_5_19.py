def count_vowels(s: str) -> int:
    """
    Counts the occurrences of vowels in a string efficiently by iterating once.
    
    Vowels considered include both lowercase and uppercase letters ('a', 'e', 'i', 
    'o', 'u'). The function avoids redundant checks using a predefined set for O(1) lookup.

    Args:
        s (str): The input string to analyze.

    Returns:
        int: Total count of vowel occurrences in the string.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert string to lowercase for case-insensitive comparison without modifying original if not needed, 
    # though iterating directly with set check is also valid and avoids extra memory allocation if s is large.
    count = 0
    
    for char in s:
        if char.lower() in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! This sentence contains many vowels like aeiou."
    
    # Hard-coded sample values as per requirements (no input(), sys.stdin, argparse)
    result_count = count_vowels(sample_string)
    
    print(f"Vowel count in '{sample_string}': {result_count}")