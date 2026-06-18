def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return text
    
    result = []
    
    # Split into words while keeping track of boundaries to handle punctuation correctly
    # We iterate character by character to maintain control over capitalization rules
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        # Check if we are at the start of a word (after space, tab, newline or after punctuation that ends a word contextually)
        # A simpler approach for "first letter of each word" usually implies splitting by whitespace and title-casing parts.
        # However, to strictly follow "capitalizing only the first letter... preserving rest", 
        # we treat sequences separated by non-alphanumeric characters as words if that's standard behavior expected.
        # Standard interpretation: split on whitespace -> capitalize each part? Or char-by-char logic?
        
        # Let's use a robust method: Split into tokens (words) based on alphanumeric continuity, then reconstruct.
        # But the prompt says "first letter of each word". 
        # Common definition: A sequence of letters separated by non-letters or spaces.
        # To be safe and efficient without external libs like re if possible, we'll use split() for whitespace words first?
        # Actually, standard title case usually ignores punctuation casing (e.g., "hello-world" -> "Hello-World").
        
        # Let's implement a character-by-character approach that identifies the start of a word.
        # A new word starts if:
        # 1. We are at index 0 and current char is alpha.
        # 2. Previous non-alphabetic char was followed by an alphabetic one (start after space/tab/newline).
        
        pass

    # Re-evaluating for efficiency and correctness without regex imports if possible, 
    # but using split() on whitespace then joining with title case is the most robust "word" definition in Python.
    # However, standard `title()` capitalizes too much (e.g., 'hello world' -> 'Hello World', correct).
    # But what about 'a.b.c'? Title usually does 'A.B.C'. 
    # The prompt asks for "first letter of each word". In natural language processing without regex:
    # Words are typically separated by whitespace. If the input is a sentence, split() works well.
    
    words = text.split()
    capitalized_words = []
    
    for w in words:
        if not w:
            continue
        # Capitalize first letter, keep rest as is (lowercase or original)
        # Python's capitalize method lowercases the whole string then uppercases first. 
        # We want to preserve existing casing of non-first letters? "preserving the rest of the casing".
        # Example: 'hElLo' -> 'HElLo'? Or just 'Hello'?
        # Prompt says: "capitalizes only the first letter ... preserving the rest of the casing".
        # This implies if input is 'hElLo', output should be 'HElLo'.
        
        new_word = w[0].upper() + w[1:]
        capitalized_words.append(new_word)
    
    return " ".join(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies.
    test_cases = [
        "hello world",           # Standard case
        "hElLo wOrld",          # Mixed casing preservation required
        "python script example",# Multiple words
        "",                     # Empty string edge case
        "   multiple spaces   ",# Extra whitespace handling (split handles this)
    ]

    for test_input in test_cases:
        output = capitalize_words(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{output}'\n")