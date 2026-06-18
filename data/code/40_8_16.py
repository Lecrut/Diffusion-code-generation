import re

def extract_first_letters(text: str) -> list[str]:
    """
    Takes a string and returns a list of strings, where each string is 
    the first letter of a word. Words containing only punctuation are ignored.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list of single-character strings representing the first letters of words.
    """
    # Split the text into tokens based on whitespace and other non-word characters, 
    # but we need to be careful with punctuation attached to words or standalone punctuation.
    
    # Strategy: Use regex to find sequences that look like "word-like" structures (letters + optional internal punctuation)
    # However, a simpler robust approach is to split by non-letter/non-digit boundaries if we consider 
    # standard English word definition where only letters count as part of the word for this purpose.
    
    # Let's define a 'valid letter' sequence: one or more alphabetic characters possibly surrounded/intermixed with punctuation?
    # The prompt says "words containing only punctuation are correctly handled (i.e., they do not produce an output)".
    # This implies we need to identify what constitutes a word. Standard definition usually involves alphanumeric + apostrophe/hyphen, 
    # but here the constraint is specifically about ignoring pure punctuation strings like "...", "-", etc.
    
    # Refined Strategy:
    # 1. Split the string into tokens using regex that separates letters from non-letters? No, because "don't" should be one word.
    # 2. Better approach: Find all sequences of characters where at least one is a letter (a-z or A-Z). 
    #    From such a sequence, take the first alphabetic character found. If no letters exist in the token, ignore it?
    
    # Actually, let's look at "words". In NLP, words are often separated by spaces/punctuation.
    # But punctuation can be attached: "hello-world", "...", "!@#".
    # Requirement: Ignore tokens that consist ONLY of punctuation.
    # So if a token is just ".", it yields nothing. If "h...ello" or "hello...", the word exists and starts with 'h'.
    
    # Algorithm:
    # 1. Split input by whitespace to get potential words/tokens? Or split by non-alphanumeric? 
    # Let's use regex to find all sequences of characters that contain at least one letter.
    # Then for each such sequence, extract the first character if it is a letter.
    
    tokens = re.findall(r"[^\s]+", text) # Split on whitespace
    
    result_list = []
    
    for token in tokens:
        # Check if the token contains at least one alphabetic character
        has_letter = any(c.isalpha() for c in token)
        
        if not has_letter:
            continue
            
        # Find the first letter in this token (case-insensitive check, but preserve case of found char)
        # We scan from left to right. The prompt says "first letter". 
        # Does it mean the very first character if it's a letter? Or the first alphabetic character regardless of position?
        # Usually "first letter" implies scanning until an alphabet is found or taking index 0 if alpha.
        # Given examples like "...hello", usually considered starting with 'h'. 
        # But strictly speaking, "." is not a letter. So we skip non-letters at start.
        
        first_char = None
        
        for char in token:
            if char.isalpha():
                first_char = char
                break
                
        if first_char:
            result_list.append(first_char)
            
    return result_list

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies.
    
    test_cases = [
        "Hello World!",           # Expected: ['H', 'W']
        "...",                    # Expected: [] (only punctuation)
        "don't eat...",          # Expected: ['d'] (treat don't as one word starting with d, or split? Usually kept together. If split by non-alpha, it might be different.)
                                # Let's re-evaluate the tokenization logic for 'don\'t'. 
                                # My regex [^\s]+ keeps apostrophe attached. "don't" -> has_letter=True. First alpha is 'd'. Correct.
        "!@#",                    # Expected: [] (only punctuation)
        "a-b-c",                  # Expected: ['a'] or ['-'? No, '-' not letter. So 'a' if we skip non-alpha] 
                                # Wait, does "-b" count as a word? If token is "-b", has_letter=True ('b'). First alpha is 'b'.
                                # But maybe the user considers "-" part of punctuation making it invalid? 
                                # Prompt: "words containing only punctuation". -b contains b (letter). So valid. First letter b.
        "",                       # Expected: []
    ]

    for test_input in test_cases:
        output = extract_first_letters(test_input)
        print(f"Input: '{test_input}' -> Output: {output}")