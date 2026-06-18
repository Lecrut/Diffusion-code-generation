def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of unique characters found multiple times in the sentence.
             Only alphabetic characters are considered, case-insensitive.
    """
    char_count = {}
    
    # Iterate through each character in the sentence
    for char in sentence.lower():  # Convert to lowercase for case-insensitivity
        if 'a' <= char <= 'z':  # Check if it's an alphabetic letter
            char_count[char] = char_count.get(char, 0) + 1
            
    # Collect letters that appear more than once
    repeated_letters = set()
    for char in char_count:
        if char_count[char] > 1:
            repeated_letters.add(char)
            
    return repeated_letters

if __name__ == '__main__':
    sample_sentences = [
        "Hello, World! This is a test sentence.",
        "Python programming involves loops and conditionals often."
    ]

    for text in sample_sentences:
        result = find_repeated_letters(text)
        print(f"Repeated letters in '{text}': {sorted(result)}")