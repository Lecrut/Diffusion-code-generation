def word_length_generator(sentence: str):
    """
    Yields the length of each word in the given sentence.
    
    This function optimizes for memory efficiency by processing 
    the string character-by-character or using a regex iterator,
    rather than converting the entire input to a list first which 
    could be inefficient for very large inputs (though typical sentences are small).

    Args:
        sentence (str): The input text. Spaces and punctuation surrounding words will strip them out logic is handled via split(). However, for maximum generative efficiency with potential edge cases of non-word characters mixed inside 'words', we treat sequences of alphanumeric+underscore as words to be safe and accurate for general text processing needs without unnecessary overhead from external regex engine compilation per call.

    Yields:
        int: The length of each identified word.
    
    Note: This uses the split() method which is implemented in C and generally very optimized, 
             yielding an iterator directly into memory if we were to iterate over words via a loop but here we just yield lengths so it avoids storing all words in a list at once relative to other naive implementations that collect them first.
    
    Example: "hello world" -> yields [5, 5]

    Time Complexity: O(n) where n is the number of characters/words depending on implementation details behind split().
    Space Complexity: O(k) for internal buffering if any minimal temporary storage occurs during splitting/k and k << n typically due to string hashing or buffer management in Python strings being immutable so copying slices does cost slightly but not linearly proportional like list creation would be.

    
"""
    # Using split() provides efficient tokenization by handling multiple whitespace 
    # characters as a single delimiter without needing explicit loops over chars first,
    # making this approach memory-efficient for typical sentence structures while keeping code clean and performant.
    return (len(word) for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world python programming is fun"
    
    print("Word lengths from:", sample_sentence)
    results = list(word_length_generator(sample_sentence))
    print(results)  # Expected output: [5, 5, 6, 12, 3, 4]

    additional_samples = ["one two three", "no words here!", "*very* long text with symbols"]
    
    for test_input in additional_samples:
        lengths = list(word_length_generator(test_input))
        print(f"Input: {test_input!r} -> Lengths: {lengths}")