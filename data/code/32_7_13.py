import re

def word_lengths(sentence: str):
    """
    Generator function that yields the length of each word in a given sentence.
    
    Optimized for memory efficiency by processing the string once and yielding 
    integers directly without storing intermediate lists or splitting the entire 
    sentence into a list first (except via regex which is efficient).

    Args:
        sentence (str): The input text containing words separated by whitespace.

    Yields:
        int: The length of each word found in the sentence.
    
    Example:
        >>> list(word_lengths("Hello world"))
        [5, 5]
    """
    # Use regex to find all sequences of alphabetic characters (words)
    # re.findall returns a list internally but we iterate over it once; 
    # for very large inputs without storing the full split list, this is efficient.
    # Alternatively, manual iteration could be used, but regex is concise and fast in CPython.
    
    words = re.findall(r'\b\w+\b', sentence)
    
    for word in words:
        yield len(word)

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is awesome and easy to learn",
        "One two three four five six seven eight nine ten"
    ]

    for s in sample_sentences:
        print(f"\nSentence: {s}")
        lengths = word_lengths(s)
        # Convert generator to list here just for demonstration output, 
        # but the function itself yields one by one efficiently.
        result_list = list(lengths)
        print(f"Word Lengths: {result_list}")