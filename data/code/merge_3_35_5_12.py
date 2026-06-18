import string

def count_vowels(s: str) -> dict:
    """
    Counts occurrences of each vowel in a given string efficiently.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping each vowel ('a', 'e', 'i', 'o', 'u') 
              and their uppercase counterparts to its count.
    """
    vowels = set(string.ascii_lowercase + string.ascii_uppercase)
    
    # Initialize counts for all possible vowels (lowercase and uppercase)
    counts = {v: 0 for v in vowels}

    # Iterate through the string exactly once, checking only if a character is a vowel.
    # This avoids redundant checks by using direct membership testing which 
    # is optimized internally but logically represents a single pass over characters.
    current_char_count = {}
    
    for char in s:
        if char.lower() in 'aeiou':
            lower_vowel = char.lower()
            counts[lower_vowel] += 1
            
    return counts

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_string_1 = "Hello, World! This is a test string with vowels: A, E, I, O, U."
    test_string_2 = "AEIOUaeiou" * 10 + "xyzXYZ"

    result_1 = count_vowels(test_string_1)
    print("Vowel counts for sample 1:")
    for vowel, count in sorted(result_1.items()):
        if count > 0:
            print(f"{vowel}: {count}")

    # Reset counter for the second test case to demonstrate functionality on different input.
    result_2 = {} 
    vowels_set = set(string.ascii_lowercase + string.ascii_uppercase)
    
    current_char_count = {}
    
    for char in test_string_2:
        if char.lower() in 'aeiou':
            lower_vowel = char.lower()
            counts[lower_vowel] += 1

    print("\nVowel counts for sample 2:")
    # Re-implementing the logic inline here to avoid re-imports or function call overhead 
    # if we were optimizing further, but since it's a module run once, calling count_vowels is cleaner.
    result_3 = count_vowels(test_string_2)
    
    for vowel, count in sorted(result_3.items()):
        print(f"{vowel}: {count}")

    # Verification of total counts matching expected values (optional sanity check logic omitted 
    # to keep code strictly functional as per task constraints on comments/prose).