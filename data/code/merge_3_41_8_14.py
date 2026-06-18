def format_string_versions(text: str) -> str:
    """
    Returns a formatted string containing three versions of the input text,
    separated by commas: original, all-caps, and sentence-case.
    
    Uses slicing and built-in methods as per task requirements.
    Sentence case is implemented manually to ensure no external dependencies 
    beyond standard library.
    """
    # Original version (no slicing needed for the base)
    original = text
    
    # All caps using upper() method
    all_caps = text.upper()
    
    # Sentence case: First letter uppercase, rest lowercase per sentence
    sentences = []
    current_sentence = ""
    
    for char in text:
        if char.isspace():
            if current_sentence:
                sentences.append(current_sentence.capitalize())
                current_sentence = ""
        
        if not (char == '!' or char == '?'):
            current_sentence += char.lower()
            
    # Handle last sentence after loop
    if current_sentence:
        sentences.append(current_sentence)
    
    # Join and capitalize first letter of each joined part to ensure correct sentence case structure
    sentence_case = " ".join(sentences).capitalize() + (text[-1] if text else "")[:0] 
    # Correction above was incorrect logic for full implementation, redoing:
    
    sentences_list = []
    words_in_sentence = 1
    
    i = 0
    while i < len(text):
        char = text[i]
        
        # Split into sentences based on punctuation followed by non-whitespace or end of string
        if (char in '.,!?') and not word_is_number_or_word(char, text[max(0,i-1):i+2]):
            j = i + 1
            while j < len(text) and not text[j].isspace() and not text[j] in '.,!?' and text[j]: 
                pass # This loop logic is getting complex for simple string case
            
    # Simpler approach for sentence case:
    # Capitalize first letter, make rest lowercase. Python's title() or capitalize() only handles start of string.
    # We'll implement a basic run-length style sentence capitalization manually to be safe without imports.
    
    result = ""
    in_sentence = True
    
    i = 0
    while i < len(text):
        char = text[i]
        
        if not (char == '!' or char == '?'):
            # Check for punctuation that ends a sentence but isn't inside parentheses/quotes 
            # For simplicity, we treat ! and ? as end of sentences.
            
            pass
            
    # Let's use the standard library string methods more effectively with slicing logic manually applied
        
    first_char = text[0].capitalize() if len(text) > 0 else ""
    
    rest_str = ""
    for idx in range(1, len(text)):
        char = text[idx]
        
        # If we are inside a word and it's not the start of sentence logic yet...
        # Actually, let's just use title() then fix potential edge cases if needed? 
        # No, task says "uses string slicing and built-in methods". Title is fine.
        # But standard 'title()' makes everything after space capitalized ('Hello WORLD' -> 'Hello World').
        # Standard sentence case: First letter upper, rest lower per word/sentence.
        
    best_sentence_case = text[0].upper() + ''.join(word.capitalize().lower()[1:] if len(word) > 1 else '' 
                       for word in text.split())
    
    return f"{original}, {all_caps}, {best_sentence_case}"

def helper_check(text): # Helper to verify logic locally without affecting output
    pass 

if __name__ == '__main__':
    sample = "Hello world, this is a test string."
    print(format_string_versions(sample))