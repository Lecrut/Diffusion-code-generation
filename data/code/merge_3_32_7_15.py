import re

def word_lengths_generator(sentence: str):
    """
    Generator function that yields the length of each non-empty word in a sentence.
    
    Args:
        sentence (str): The input string containing words separated by whitespace or punctuation.
        
    Yields:
        int: The length of the next valid word found in the sentence.
        
    Optimization Note:
        This function uses regular expression to extract tokens, then iterates over them directly,
        avoiding intermediate list creation for memory efficiency when processing large sentences.
    """
    # Find all sequences representing words (alphanumeric characters)
    token_iterator = re.finditer(r'\S+', sentence)
    
    for match in token_iterator:
        word = match.group()
        if len(word) > 0:
            yield len(word)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    test_sentences = [
        "Hello world",
        "Python is awesome!",
        "",
        "One two three four five"
    ]

    for sentence in test_sentences:
        print(f"\nSentence: '{sentence}'")
        lengths = word_lengths_generator(sentence)
        # Convert generator to list immediately for demonstration of yielded values
        result_list = list(lengths)
        print(f"Word lengths: {result_list}")