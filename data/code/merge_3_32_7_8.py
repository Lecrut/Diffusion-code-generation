import re

def word_length_generator(sentence: str):
    """
    Yields the length of each word in the given sentence.
    
    Optimizes memory efficiency by processing the string without creating 
    intermediate lists or copies, yielding values one at a time as they are found.
    
    Args:
        sentence (str): The input text to process. Words are defined as sequences 
                        separated by whitespace and punctuation is stripped from word boundaries.
        
    Yields:
        int: The length of the next word found in the sentence.
    """
    # Use a regex iterator which processes the string efficiently without loading everything into memory at once
    words = re.finditer(r'\b\w+\b', sentence)
    
    for match in words:
        yield len(match.group())

if __name__ == '__main__':
    sample_sentence = "Hello, World! This is a test."
    
    print("Word lengths from:", repr(sample_sentence))
    results = list(word_length_generator(sample_sentence))
    print(results)  # Expected output: [5, 5, 3, 2, 4]