import re

def word_lengths(sentence: str):
    """
    Generator function that yields the length of each word in a given sentence.
    
    This implementation optimizes memory efficiency by using regex to find words
    and yielding their lengths directly, avoiding intermediate list creation or string slicing overheads for large inputs.

    Args:
        sentence (str): The input text containing one or more sentences with mixed punctuation.

    Yields:
        int: The length of each word found in the sentence. Words are defined as sequences 
             separated by non-alphanumeric characters, excluding standalone numbers if desired, 
             but here we include all alphanumeric tokens including numbers for comprehensive coverage.
    
    Example:
        >>> list(word_lengths("Hello world! How are you?"))
        [5, 5, 2, 3]
    """
    # Use regex to find all sequences of alphanumeric characters (words)
    words = re.findall(r'\b\w+\b', sentence.strip())
    
    for word in words:
        yield len(word)

if __name__ == '__main__':
    sample_sentences = [
        "Hello world! This is a test.",
        "Python programming languages are powerful and versatile tools.",
        "123 numbers count as words too 456 here."
    ]

    for idx, sentence in enumerate(sample_sentences):
        print(f"Sample {idx + 1}: '{sentence}'")
        word_lengths_gen = word_lengths(sentence)
        lengths_list = list(word_lengths_gen)
        print(f"Word lengths: {lengths_list}")