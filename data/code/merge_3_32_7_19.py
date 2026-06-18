import re

def get_word_lengths(sentence: str):
    """
    Generator function that yields the length of each word in a given sentence.
    
    Optimized for memory efficiency by using regex to find words directly 
    without loading the entire text into lists or intermediate structures.
    
    Args:
        sentence (str): The input string containing words separated by whitespace.
        
    Yields:
        int: The length of each word found in the sentence.
    """
    # Use a regex iterator to find all words directly without storing them in memory first
    for match in re.finditer(r'\w+', sentence):
        yield len(match.group())

if __name__ == '__main__':
    sample_sentence = "Hello world, this is an example of a generator function."
    
    # Calculate lengths using the generator and print results immediately to avoid storing all values
    for length in get_word_lengths(sample_sentence):
        print(length)