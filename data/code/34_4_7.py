import sys

def capitalize_first_letters(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character of each word capitalized,
             preserving all other characters exactly as they were.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    words = text.split()
    result_words = []

    for i, word in enumerate(words):
        if len(word) > 0:
            # Capitalize only the first character of the current word
            capitalized_word = word[0].upper() + word[1:]
            result_words.append(capitalized_word)
            
            # If it was not the last word, add a space back to reconstruct sentence structure
            if i < len(words) - 1:
                result_words.append(' ')

    return ''.join(result_words)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or network access is required.
    samples = [
        "hello world",
        "python programming language",
        "the quick brown fox jumps over the lazy dog"
    ]

    for sample in samples:
        output_text = capitalize_first_letters(sample)
        print(f'Input: "{sample}"')
        print(f'Output: "{output_text}"\n')