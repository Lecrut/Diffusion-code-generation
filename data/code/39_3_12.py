import re

def extract_words_from_text(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process. Can contain newlines and various punctuation.
        
    Returns:
        list[str]: A list containing the extracted words in their original order.
    """
    # Using regular expression to find all sequences of alphanumeric characters [a-zA-Z0-9]
    matches = re.findall(r'[a-zA-Z0-9]+', text)
    return matches

if __name__ == '__main__':
    sample_input_text = "Hello World! This is a multi-line example. 12345 Words, numbers and symbols here."

    result_words = extract_words_from_text(sample_input_text)

    print("Extracted words:")
    for word in result_words:
        print(f"{word}")