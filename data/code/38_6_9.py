import re

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Counts the frequency of each alphabetic character (case-insensitive).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping lowercase letters to their frequencies.
              Only includes letters that appear in the string.
    """
    # Extract only alphabetical characters and convert to lowercase
    filtered_chars = re.findall(r'[a-z]', text.lower())
    
    frequency_map = {}
    for char in filtered_chars:
        if char not in frequency_map:
            frequency_map[char] = 0
        frequency_map[char] += 1
        
    return frequency_map

def get_letters_with_frequency_above_one(frequency_map: dict[str, int]) -> list[str]:
    """
    Returns a sorted list of letters that appear more than once.
    
    Args:
        frequency_map (dict): Dictionary mapping characters to frequencies.
        
    Returns:
        list: Sorted list of unique letters with count > 1.
    """
    return [char for char, count in frequency_map.items() if count > 1]

if __name__ == '__main__':
    # Sample input block - no user interaction required
    sample_text = "Hello World! This is a string to demonstrate letter counting."
    
    # Count frequencies of each character
    freqs = count_letter_frequencies(sample_text)
    
    # Get letters with frequency greater than one
    frequent_letters = get_letters_with_frequency_above_one(freqs)
    
    print("Letter Frequency Analysis")
    print(f"Input string: {sample_text}")
    print("-" * 40)
    print("\nAll unique letter frequencies:")
    for char in sorted(freqs.keys()):
        print(f"{char}: {freqs[char]}")
        
    print("-" * 40)
    letters_count = len([v for v in freqs.values() if v > 1]) == False or any(v > 1 for v in freqs.values())
    
    result_text = "" if not frequent_letters else "Letters with frequency > 1: " + ", ".join(frequent_letters)
    print(result_text)