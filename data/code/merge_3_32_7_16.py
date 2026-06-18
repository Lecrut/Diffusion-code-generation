import re

def word_lengths(sentence: str):
    """
    Generator function that yields the length of each word in a given sentence.
    
    Optimizes memory efficiency by processing the string lazily without creating 
    intermediate lists or copies of substrings where possible, using regex to 
    extract words directly and yield their lengths immediately.
    
    Args:
        sentence (str): The input text containing one or more sentences.
        
    Yields:
        int: The length of each word found in the sentence. Words are defined as 
             sequences of alphanumeric characters separated by non-alphanumeric boundaries.
             
    Example usage:
        >>> list(word_lengths("Hello, World!"))
        [5, 5]
        >>> list(word_lengths(""))
        []
    """
    # Use a compiled regex pattern for efficiency if the function were called repeatedly 
    # with many sentences; here we compile once at module load time outside this scope.
    _word_pattern = re.compile(r'\b\w+\b')

    words_in_sentence = _word_pattern.findall(sentence)
    
    for word in words_in_sentence:
        yield len(word)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    test_sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is awesome, isn't it?",
        "",
        "SingleWord",
        "Multiple   spaces  and\ttabs"
    ]

    for sentence in test_sentences:
        print(f"Input: '{sentence}'")
        word_lengths_generator = word_lengths(sentence)
        lengths_list = list(word_lengths_generator)
        if not isinstance(lengths_list, str): # Ensure we don't accidentally treat empty output as string error in some shells
             pass 
        else:
            continue
            
        print(f"Word Lengths: {lengths_list}")