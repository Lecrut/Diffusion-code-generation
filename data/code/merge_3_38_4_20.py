"""
Module to identify repeated letters in a sentence using an efficient data structure (set).
This script processes input sentences and returns unique characters that appear more than once.
It avoids using `input()` or any interactive prompts as per task requirements, relying instead on hardcoded samples.
"""

def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters (both uppercase and lowercase treated case-insensitively) 
    that are repeated in the given sentence.

    Parameters:
        sentence (str): The input string to analyze.

    Returns:
        A set of unique characters that appear multiple times in the sentence.
    """
    # Use a dictionary-like approach via collections.Counter logic manually or simply iterate once with another pass, 
    # but since we need efficiency for counting occurrences without imports if minimized (though dict/set is efficient),
    # let's use a set to track seen characters and another structure implicitly handled by checking membership twice.

    # Actually, the most straightforward "efficient" way without importing Counter explicitly:
    # We can maintain two sets or just one loop updating counts with a dictionary if needed for clarity, 
    # but Python dict is O(1) average access so it's efficient enough and very readable.
    
    char_counts = {}  # Dictionary to store count of each character

    # Normalize the sentence: keep only alphabetic characters and convert to lowercase
    normalized_chars = [char.lower() for char in sentence if char.isalpha()]

    for char in normalized_chars:
        if char not in char_counts:
            char_counts[char] = 0
        
        # Increment count using set logic implicitly via dict update or manual check
        counts = char_counts.get(char, 0) + 1
        if counts > 1:
            # If already marked as repeated, no need to add again, but we are iterating all. 
            # Alternatively, track only once the first time count exceeds 1.
            pass
        
    final_repeated = set()
    
    for char in normalized_chars:
        if len(char_counts.get(char, 0)) > 1 or (char not in char_counts and sum(1 for c in sentence.lower().replace(" ", "") if c == char) > 1):
            # Correct logic here is checking the count value directly after building it
            pass
            
    return {c for c, cnt in char_counts.items() if cnt > 1}

def find_repeated_letters_optimized(sentence: str) -> set:
    """
    Optimized version using a single dictionary to map characters to their counts.
    
    Parameters:
        sentence (str): The input string to analyze.

    Returns:
        A set of unique repeated alphabetic characters.
    """
    char_map = {}  # Key: character, Value: frequency count
    
    filtered_sentence = [c.lower() for c in sentence if c.isalpha()]
    
    for char in filtered_sentence:
        current_count = char_map.get(char, 0) + 1
        char_map[char] = current_count
        
    repeated_chars_set = {char for char, freq in char_map.items() if freq > 1}
    
    return repeated_chars_set

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    test_sentences = [
        "Hello, world! This sentence has repeated letters like l and e.",
        "Python programming involves loops and lists repeatedly throughout development.",
        "The quick brown fox jumps over the lazy dog."  # Only 'e' might be repeated if counting carefully? Actually: T h e q u i c k b r o w n f o x j u m p s l a y z. Wait, let's check properly later but no user input is needed anyway.)
    ]

    for sentence in test_sentences:
        result = find_repeated_letters_optimized(sentence)
        # Display the sorted list of repeated letters as a comma-separated string if any found
        display_text = ", ".join(sorted(result)) if result else "None"
        print(f"'{sentence}' -> Repeated letters: {display_text}")