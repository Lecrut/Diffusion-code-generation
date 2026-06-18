def sentence_word_length_generator(sentence: str):
    """
    Yields the length of each word in a given sentence.
    
    This function optimizes memory efficiency by not storing all words or lengths 
    in a list; instead, it processes and yields them one at a time as strings are split.
    
    Args:
        sentence (str): The input string containing the text to process.
        
    Yields:
        int: The length of each word found in the sentence.
    """
    # Split the sentence into words based on whitespace, handling multiple spaces automatically
    for word in sentence.split():
        if len(word) > 0:  # Ensure we only yield non-empty tokens (e.g., trailing newlines might create empty strings)
            yield len(word)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, no user input or files used.
    samples = [
        "The quick brown fox jumps over the lazy dog",
        "Python is awesome and efficient.",
        "",  # Edge case: empty string
        "   multiple      spaces   between words ",
    ]

    for sample in samples:
        print(f"Input: '{sample}'")
        lengths = sentence_word_length_generator(sample)
        result_list = list(lengths)
        print(f"Word Lengths: {result_list}")