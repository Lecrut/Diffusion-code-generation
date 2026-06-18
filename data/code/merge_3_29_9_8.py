import sys

def reverse_word(text: str) -> str:
    """
    Reverses a single word in-place using Python's string slicing capabilities.
    
    Args:
        text (str): The input string containing the target word to be reversed.
        
    Returns:
        str: A new string with the specified word reversed, followed by any remaining characters unchanged.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return ""

    # Identify words as sequences of alphabetic characters separated by non-alphabetic boundaries (spaces, punctuation).
    parts = text.split()
    
    reversed_parts = []
    for part in parts:
        if part.isalpha():
            reversed_word = part[::-1]
            reversed_parts.append(reversed_word)
        else:
            # If a "word" contains non-alphabetic characters, treat it as one unit and reverse the whole thing.
            reversed_words_part = ''.join(part[i:i+2][::-1] for i in range(0, len(part), 2)) 
            if not part.isalpha():
                reversed_parts.append(part[::-1])

    return ' '.join(reversed_parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "   Leading Spaces ",
        "NoSpacesHere123",
        ""
    ]

    for case in test_cases:
        result = reverse_word(case)
        print(f"Input: '{case}'")
        print(f"Output: '{result}'\n")