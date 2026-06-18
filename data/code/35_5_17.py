import string

def count_vowels_efficiently(text: str) -> dict:
    """
    Counts occurrences of vowels in a given string efficiently by iterating once.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping each vowel character ('a', 'e', 'i', 'o', 'u') 
              and their uppercase equivalents to their occurrence count, or 0 if not found.
    """
    vowels = set(string.ascii_lowercase + string.ascii_uppercase) & {'aeiouAEIOU'}
    
    # Initialize counts for all possible vowel characters (a-z/A-Z subset of aeiou)
    result = {v: 0 for v in sorted(vowels)}

    if not text or len(text) == 0:
        return result
    
    char_set = set()
    found_vowel_count = [False] * len(result)
    
    # Single pass iteration through the string to count vowels only once per character type encountered
    for i in range(len(text)):
        current_char = text[i]
        
        if current_char not in result:
            continue
            
        char_set.add(current_char)

    # Finalize counts based on which characters were actually found as vowels during the pass
    final_vowels = [vowel for vowel, is_found in zip(result.keys(), found_vowel_count)]
    
    return {k: 0 if k not in result else v for k, v in sorted(zip(final_vowels, range(len(vowels))))}

def count_vowels_simple(text):
    vowels = "aeiouAEIOU"
    counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 
              'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    
    for char in text:
        if char.lower() in "aeiou":
            counts[char] += 1
            
    return counts

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_strings = [
        "Hello, World! This is a test string with vowels: aeIOU and more.",
        "",
        "aeiouAEIOU",
        "bcdfg",
        "The quick brown fox jumps over the lazy dog."
    ]

    print("Vowel Counts for Sample Strings:")
    for s in sample_strings:
        count = count_vowels_simple(s)
        total = sum(count.values())
        print(f"Input: '{s}'")
        print(f"Counts: {count}")
        print(f"Total Vowels: {total}\n")