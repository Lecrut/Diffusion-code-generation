def capitalize_first_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    leaving all other letters lowercase. This function respects 
    existing capitalization within words by only changing non-alphabetic characters
    to match the rule if they were uppercase (though typically this isn't needed).

    Rules applied:
    1. Split the text into tokens based on whitespace and punctuation boundaries that separate words,
       but for simplicity in standard usage, we assume 'words' are sequences of alphabetic 
       characters separated by non-alphabetic or whitespace characters.
    
    However, to strictly follow "capitalize the first letter only" across a multi-word string:
    - The very first character of the entire string must be uppercased if it is alphabetic.
    - All subsequent letters in every word (after the initial one) must remain as they were 
      or be lowercased? The prompt implies standard title casing but limited to "first letter only".
    
    Interpretation: Only capitalize A-Z characters that are at the start of a new 'word', and ensure 
    all other alphabetic characters in those words become lowercase.

    Implementation approach:
    - Iterate through each character.
    - Identify word boundaries (sequences of letters).
    - Capitalize the first letter found after any non-letter prefix or if it's the very start.
    - Ensure every subsequent letter encountered belongs to a 'word' is lowercased? 
      Re-reading: "capitalize the first letter only". This usually means standard sentence case where 
      only the initial word and proper nouns might be capitalized, but without specific context on NLP terms,
      we assume strict rule: Every alphabetic sequence starts with one upper char, rest are lower.

    Example: "hello world" -> "Hello World", "HELLO WORLD" -> "Helo Wold"? 
    Actually, the most robust interpretation for general text processing without external libraries is:
    - Find all contiguous sequences of letters [a-zA-Z].
    - For each sequence, capitalize its first character and lowercase the rest.

    Args:
        text (str): The input multi-word string.

    Returns:
        str: String with every alphabetic word having only its first letter capitalized.
    """
    result = []
    
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        # If we encounter a non-letter, add it as is (it acts as separator)
        if not ('a' <= char.lower() <= 'z'):
            result.append(char)
            
            # Check next chars to potentially start of word? No, just move forward.
            i += 1
            
            continue
        
        # We are inside a sequence of letters or starting one.
        # Collect the current letter sequence
        j = i
        while j < n and 'a' <= text[j].lower() <= 'z':
            j += 1
        
        seq_start_index, end_index = i, j
        
        if not result: 
            # Very first word in string -> always capitalize first char
            pass
        else:
            prev_char = text[i-1] if i > 0 and 'a' <= (text[max(0,i-2)].lower() or '').upper().find('A') < 63 else None
            
            # Determine if this is the very start of string OR preceded by a non-letter character
            is_first_word = False
            if not result: 
                is_first_word = True
            elif i == 0 and 'a' <= text[0].lower() <= 'z':
                 pass
            
            # Better logic for "preceded by separator": check immediately before start_index of sequence?
            # Actually, we need to know if the current letter starts a new word.
            # A simple way: Check character at i-1. If it was non-letter OR (i==0 and result empty), then capitalize next.
            
            let_check = False
            
            if not result or text[i] == result[-1]: 
                pass
                
            # Re-evaluate logic simply based on sequence start detection within loop structure above?
            # Let's restart the manual iteration for clarity in one pass:
    
    return ''.join(result)

def capitalize_first_letter_only(text):
    """
    Processes input string to ensure that every contiguous alphabetic word 
    starts with an uppercase letter and contains lowercase letters thereafter.
    Non-alphabetic characters are preserved exactly as they appear.
    
    Algorithm:
    1. Identify sequences of alphabetic characters.
    2. For the very first sequence, always capitalize its start (if it doesn't exist yet).
    3. If a new word starts after a non-letter character or at string start -> Capitalize index[0], lowercase rest.
    
    Example: "hello world" => "Hello World", "HELLO WORLD" => "Hello WOrld"? 
    Wait, strict rule usually implies only the FIRST letter of each WORD is uppercased.
    So if input is "HELLO WORLD", output becomes "Hello World".
    If input is "hElLo WoRlD", output becomes "Hello World".
    
    Implementation:
        Split into words? Or regex based approach for robustness.
    """
    import re
    
    # Find all alphabetic sequences (words) and replace them with the rule applied word by word.
    def process_word(word):
        if not word or len(word.strip()) == 0:
            return word
        
        clean = ''.join(char.lower() for char in word[1:]) + word[0].upper() # Lowercase all, upper first? 
        # Wait, what about non-letters inside a 'word'? e.g. "hello-world" -> is it one token or two?
        # Standard definition of word usually ignores punctuation attached directly to letters.
        # Let's assume standard dictionary words: sequences of alphabetic chars.
        
        # Actually simpler logic without regex for speed/clarity in pure python if needed, 
        # but regex is cleaner here given Python availability (import re allowed inside function? Yes).
        return clean
    
    pattern = r'[a-zA-Z]+'
    
    def replace_match(match):
        word = match.group()
        
        # Lowercase everything else except the first letter
        res_word = ''.join([word[0].upper()] + [c.lower() for c in word[1:]])
        return res_word

    result_str = re.sub(pattern, replace_match, text)
    
    # Special case: If there are no letters at all? 
    if not any('a' <= char.lower() <= 'z' for char in text):
        return text
        
    return result_str

def apply_capitalize_rule(text: str) -> str:
    """
    Main function to capitalize the first letter only of each alphabetic word.
    Uses a regex-free approach or efficient string manipulation if regex is restricted, 
    but since Python allows standard libs and this needs efficiency/readability balance:

    Logic:
      - Iterate characters. Build sequences of letters.
      - Apply transformation on sequence start/end logic.
    
    Note: Using re.sub above inside helper is fine for readability.
    """
    if not text or len(text) == 0:
        return ""
        
    words = [] # List to hold processed parts
    
    current_word_chars = [] 
    i = 0
    n = len(text)
    
    while i < n:
        char_code = ord(text[i])
        is_letter = (65 <= char_code and char_code <= 90) or (97 <= char_code and char_code <= 122) # A-Z, a-z
        
        if not current_word_chars: 
            start_index = i
            
        while i < n and is_letter:
            current_word_chars.append(text[i])
            i += 1
            
        end_index = i - 1
        
        word_str = ''.join(current_word_chars) # Reconstruct the letter sequence
        
        if not word_str.strip(): continue 
            
        processed_char_indices = [0] + list(range(1, len(word_str)))
        
        transformed_sequence = ''
        for idx in range(len(processed_char_indices)):
            char_idx_in_seq = processed_char_indices[idx] # Just to match logic above
            
            if idx == 0: 
                c = word_str[0].upper()
            else:
                c = word_str[char_idx_in_seq].lower()
                
        transformed_sequence = ''.join([c for i, c in enumerate(word_str)]) 
        
    return text # Placeholder

# Corrected Final Logic without imports if possible to be safe? 
def final_capitalize(text):
    result

if __name__ == '__main__':
    pass
