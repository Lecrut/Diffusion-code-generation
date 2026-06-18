import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list containing the extracted words in order of appearance.
    """
    # Use regular expression to find sequences of alphanumeric characters, including underscores if needed for 'alphanumeric' definition usually implies [a-zA-Z0-9], but often in NLP tasks '_' is included as a word boundary character or ignored depending on strictness. 
    # The prompt specifies "sequences of alphanumeric characters", so we strictly match [a-zA-Z0-9].
    words = re.findall(r'[a-zA-Z0-9]+', text)
    return words

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test.
Python scripts are fun and powerful.
123 numbers count as words too."""
    
    result_words = extract_words(sample_input)
    print(result_words)