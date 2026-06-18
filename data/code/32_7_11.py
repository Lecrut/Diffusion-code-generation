def word_length_generator(sentence: str):
    """
    Generator function that yields the length of each word in a given sentence.
    
    Optimizes memory efficiency by processing tokens one at a time instead 
    creating intermediate lists or splitting strings into large parts if not needed,
    although string split inherently creates list objects, this implementation avoids
    additional data structures and unnecessary iterations over words.

    Args:
        sentence (str): The input sentence containing spaces to separate words.

    Yields:
        int: The length of the next word found in the sentence.
    
    Example usage: 
        >>> list(word_length_generator("Hello world"))
        [5, 5]
    """
    # Split string into tokens (words) separated by whitespace
    words = sentence.split()

    for word in words:
        yield len(word)

if __name__ == '__main__':
    sample_sentences = [
        "Python is a great programming language",
        "",
        "A",
        "One two three four five six seven eight nine ten"
    ]

    for idx, sentence in enumerate(sample_sentences):
        print(f"\nSample {idx + 1}: '{sentence}'")
        
        # Generate and collect lengths to verify output (for demonstration)
        result = list(word_length_generator(sentence))
        
        if not sentence.strip():
            print("Result: []")
        else:
            for length in result:
                print(length, end=" ")
        print()  # Newline after each sample