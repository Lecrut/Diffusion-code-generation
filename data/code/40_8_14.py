import re

def extract_first_letters(text: str) -> list[str]:
    """
    Takes a string and returns a list of strings, where each string is 
    the first letter of a word. Words containing only punctuation are ignored.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the first letters of words.
    """
    # Split the text into tokens based on whitespace and other non-word characters, 
    # but we need to be careful with punctuation attached to words.
    # We will use a regex approach to find sequences of alphanumeric characters (words).
    
    # Find all contiguous sequences of letters and digits. This effectively ignores
    # standalone punctuation or punctuation surrounded by spaces that don't form part of a word.
    # Example: "Hello, world!" -> ["Hello", "world"]
    words = re.findall(r'\b\w+\b', text)
    
    result_list = []
    for word in words:
        if not word:  # Safety check, though regex \b\w+ should avoid empty strings
            continue
        
        first_char = word[0]
        
        # Ensure the character is actually a letter (a-z or A-Z) to exclude numbers 
        # if strictly "letter" was implied, but typically 'word' implies alphanumeric.
        # The prompt says "first letter", so we should filter out digits too?
        # Re-reading: "words containing only punctuation are correctly handled".
        # Usually, a word like "123" is considered a string of words/digits in regex \w+.
        # However, the term "letter" implies [a-zA-Z]. Let's filter to ensure it's an alphabetic char.
        
        if first_char.isalpha():
            result_list.append(first_char)
            
    return result_list

if __name__ == '__main__':
    sample_inputs = [
        "Hello, world!",
        "... !!! ...",
        "Python 3 is great.",
        "One, two three...",
        "",
        "No punctuation here."
    ]

    for test_input in sample_inputs:
        output = extract_first_letters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: {output}")
        print("-" * 20)