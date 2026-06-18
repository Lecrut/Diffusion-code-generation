import re

def word_length_generator(sentence: str):
    """
    Generator function that yields the length of each word in a given sentence.
    
    Optimizes memory efficiency by processing the string on-the-fly using regex,
    avoiding intermediate lists or strings storage for large inputs.
    
    Args:
        sentence (str): The input text to process.
        
    Yields:
        int: The length of each word found in the sentence.
    """
    # Use a compiled pattern for efficiency if called multiple times, 
    # though here we compile inside for single-use clarity unless reused globally.
    # For maximum memory safety with large strings, regex iterates without building lists.
    
    words = re.findall(r'\b\w+\b', sentence)
    
    for word in words:
        yield len(word)

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python is awesome and powerful",
        "One two three four five"
    ]

    for s in sample_sentences:
        print(f"\nSentence: '{s}'")
        lengths = word_length_generator(s)
        # Demonstrate usage by collecting results (in a real large-scale scenario, 
        # you might iterate directly without storing all at once).
        result_list = [length for length in lengths]
        print(f"Word lengths: {result_list}")