import re

def word_length_generator(sentence: str):
    """
    Generator function that yields the length of each word in a given sentence.
    
    This implementation optimizes for memory efficiency by processing the input string
    on-the-fly using regular expressions to extract words and their lengths without 
    creating intermediate lists or full tokenized copies if unnecessary (though regex 
    compilation is done once). Non-alphanumeric characters are ignored as delimiters,
    preserving whitespace structure implicitly through iteration.

    Args:
        sentence (str): The input string containing the sentence with potential punctuation.

    Yields:
        int: The length of each word found in the sentence.

    Example:
        >>> list(word_length_generator("Hello, world!"))
        [5, 5]
    """
    # Use a compiled regex pattern for efficiency if called repeatedly (though per task 
    # requirements we keep it simple here; compiling inside is negligible overhead for single use).
    # Pattern: matches sequences of alphanumeric characters.
    word_pattern = re.compile(r'\w+')

    for match in word_pattern.finditer(sentence):
        yield len(match.group())

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "Python is great.",
        "One two three four five",
        "No punctuation here at all!"
    ]

    for i, sentence in enumerate(sample_sentences):
        print(f"Sample {i + 1}: '{sentence}'")
        lengths = list(word_length_generator(sentence))
        print("Word lengths:", lengths)