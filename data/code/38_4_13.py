import string

def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.
    
    Args:
        sentence (str): The input text to analyze.
        
    Returns:
        set: A set of unique characters found at least twice, ignoring case and non-letter chars.
    """
    # Filter for alphabetic characters only and convert to lowercase
    letters = [char.lower() for char in sentence if char.isalpha()]
    
    frequency_map = {}
    
    # Iterate through the filtered list to count occurrences efficiently using a dictionary
    for letter in letters:
        if letter in frequency_map:
            frequency_map[letter] += 1
        else:
            frequency_map[letter] = 1
            
    # Extract keys where value (count) is greater than 1
    repeated_letters = {char for char, count in frequency_map.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive prompts
    sample_sentences = [
        "Hello, world!",
        "A man a plan a canal Panama",
        "The quick brown fox jumps over the lazy dog"
    ]

    for sentence in sample_sentences:
        result = find_repeated_letters(sentence)
        
        # Sort letters alphabetically for consistent output display
        sorted_result = "".join(sorted(result))
        print(f"In '{sentence}': Repeated letters are {sorted_result}")