import re

def find_repeated_letters(text: str) -> list[str]:
    """
    Finds all letters that appear more than once in the input string, 
    ignoring case and non-alphabetic characters. Returns a sorted list of unique repeated letters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        List[str]: A sorted list of uppercase letters found multiple times in the string.
    """
    # Convert to lowercase and keep only alphabetic characters
    filtered_text = re.sub(r'[^a-z]', '', text.lower())
    
    letter_counts = {}
    for char in filtered_text:
        if 'a' <= char <= 'z':  # Ensure we are dealing with letters
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
    repeated_letters = [char for char, count in letter_counts.items() if count > 1]
    
    return sorted(repeated_letters)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    test_cases = [
        "hello world",
        "Python scripting is fun!",
        "aabbccdd",
        "The quick brown fox jumps over the lazy dog.",
        "No repetition here at all"
    ]

    for text in test_cases:
        repeated = find_repeated_letters(text)
        if not repeated:
            print(f"No repeated letters found in: '{text}'")
        else:
            print(f"Repeated letters in: '{text}' are {repeated}")