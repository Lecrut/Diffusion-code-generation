def count_vowels(text: str) -> int:
    """Counts the total number of vowels in a given string, case-insensitive."""
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert input to lowercase for case-insensitive comparison and iterate through characters
    lower_text = text.lower()
    count = 0
    
    for char in lower_text:
        if char in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    
    # Sample string with multiple vowels of different cases and punctuation mixed in.
    sample_string_1 = "Hello, World! How are you?"
    
    # Test case 2: String with only uppercase letters containing vowels.
    sample_string_2 = "AEIOU"
    
    # Test case 3: Empty string edge case (optional extension for robustness).
    empty_string_test = ""
    
    print(f"Input: '{sample_string_1}'")
    result_1 = count_vowels(sample_string_1)
    print(f"Vowel Count in Sample 1: {result_1}")
    
    print(f"\nInput: '{sample_string_2}'")
    result_2 = count_vowels(sample_string_2)
    print(f"Vowel Count in Sample 2: {result_2}")
    
    print(f"\nInput: '{empty_string_test}'")
    result_empty = count_vowels(empty_string_test)
    print(f"Vowel Count in Empty Test: {result_empty}")

# Example of manual usage logic if needed outside the main block (for clarity only):
def validate_input(data: str) -> bool:
    """Validates that input is a string."""
    return isinstance(data, str) and data != None