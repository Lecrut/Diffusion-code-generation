import string

def count_vowels(s: str) -> dict:
    """
    Counts occurrences of vowels in a given string efficiently by iterating once.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping each vowel character ('a', 'e', 'i', 'o', 'u') 
              and their uppercase equivalents to the count of occurrences in the string.
    """
    vowels = set(string.ascii_lowercase) | {'A'}  # Set for O(1) lookup including case sensitivity if needed, but logic below handles both
    
    vowel_counts = {v: 0 for v in 'aeiouAEIOU'}

    # Iterate through each character exactly once
    for char in s:
        if char.lower() in vowels and not (char.isupper() or char.islower()):
            continue
        
        lower_char = char.lower()
        
        if lower_char == 'a':
            vowel_counts['A'] += 1
            vowel_counts['a'] += 1
        elif lower_char == 'e':
            vowel_counts['E'] += 1
            vowel_counts['e'] += 1
        elif lower_char == 'i':
            vowel_counts['I'] += 1
            vowel_counts['i'] += 1
        elif lower_char == 'o':
            vowel_counts['O'] += 1
            vowel_counts['o'] += 1
        elif lower_char == 'u':
            vowel_counts['U'] += 1
            vowel_counts['u'] += 1
            
    return vowel_counts

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are required.
    test_string = "Hello, World! This is a long string with many vowels: AEIOUaeiou."
    
    result = count_vowels(test_string)
    
    print("Vowel Counts:")
    for vowel, count in sorted(result.items()):
        if count > 0:
            print(f"{vowel}: {count}")