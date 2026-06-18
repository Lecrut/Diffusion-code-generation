import sys

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of each word from the input text.
    
    Args:
        text (str): The input string, potentially containing multiple lines and punctuation.
        
    Returns:
        list[str]: A list where each element is the lowercase first letter of a found word.
    """
    words = []
    for line in text.splitlines():
        # Split by whitespace to handle multi-word sentences within lines
        current_words_on_line = line.strip().split()
        
        if not current_words_on_line:
            continue
            
        for word in current_words_on_line:
            # Remove common punctuation from the start of words (e.g., "Hello!" -> "Hello")
            stripped_word = word.lstrip(string.punctuation).lstrip('_') or ''
            
            if len(stripped_word) > 0:
                words.append(stripped_word[0].lower())
    
    return words

if __name__ == '__main__':
    sample_text = """Hello World. This is a test script for production use cases."""

    result_letters = get_first_letters(sample_text)

    print(result_letters)