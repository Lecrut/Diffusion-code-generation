import string

def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Args:
        sentence (str): The input sentence to analyze.
        
    Returns:
        set: A set of unique characters found multiple times, ignoring case and non-alphabetic characters.
    """
    char_count = {}
    
    # Iterate through each character in the string
    for char in sentence.lower():  # Convert to lowercase for case-insensitive comparison
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are considered
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                
    return {char for char, count in char_count.items() if count > 1}

if __name__ == '__main__':
    # Hard-coded sample values as per instructions to avoid any input prompts or dependencies.
    test_sentences = [
        "Hello world! This is a simple sentence where letters are repeated multiple times.",
        "A man, a plan, a canal: Panama",
        "The quick brown fox jumps over the lazy dog."  # Note: 'e', 'a' and others repeat here but some may be subtle.
    ]

    for idx, test_input in enumerate(test_sentences, start=1):
        repeated = find_repeated_letters(test_input)
        if not isinstance(repeated, set):
            raise TypeError("The function must return a set of characters.")
        
        result_list = sorted(list(repeated))  # Sort alphabetically for consistent output display
        
        print(f"Test Case {idx}: '{test_input}'")
        print(f"Repeated letters: {''.join(result_list)}\n")