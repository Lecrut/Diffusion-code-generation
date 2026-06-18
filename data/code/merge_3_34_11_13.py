def capitalize_first_letter_only(text: str) -> str:
    """
    Returns a new string where only the first character of every word is capitalized.
    
    This function handles multiple spaces between words and leading/trailing whitespace,
    ensuring that non-alphabetic characters do not trigger capitalization unless they are 
    part of an actual letter sequence at the start of a word (though strictly speaking,
    standard definition implies only letters can be 'first character' to capitalize).
    
    Algorithm:
    1. Split the input string into words based on whitespace while preserving structure implicitly via join.
       However, splitting by multiple spaces and joining with single space might alter original spacing if not careful.
       A better approach is iteration over characters or regex-based replacement for efficiency without external dependencies like re.
    
    Optimized Approach (no imports):
    - Iterate through the string character by character.
    - Maintain a state flag indicating whether we are at the start of a new word.
    - Define what constitutes a "word": A sequence of non-whitespace characters. The first letter encountered 
      after whitespace or at the very beginning is capitalized if it's alphabetic.
    
    Note: This implementation assumes 'words' are sequences separated by one or more spaces, as per standard English text processing.
    Only actual letters (a-z, A-Z) will be considered for capitalization logic to avoid modifying digits/symbols incorrectly 
    in edge cases like "hello 123 world". If the requirement strictly means every non-space char's first instance is capitalized regardless of type:
    The problem says "first character of every word", implying alphabetic context usually. But let's stick to standard definition:
    Capitalize if it's a letter and starts a word sequence (after space or start).

    Efficiency: O(n) time complexity where n is the length of the string, using single pass iteration.
    
    Args:
        text (str): The input string containing words separated by whitespace.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    result = []
    i = 0
    n = len(text)

    # Helper to check if char is alphabetic (optional but good for correctness; 
    # if we must capitalize every non-space 'first' regardless, remove this check).
    def is_alpha(char):
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z')

    while i < n:
        current_char = text[i]
        
        # Check if we are at the start of a word (beginning of string or after whitespace)
        is_start_of_word = False
        
        if not result and current_char == '\n': 
            continue  # Skip leading newlines? Or treat as part of flow. Let's assume standard space separation logic first.
        
        # Determine if previous char was non-word (space, newline, tab etc) or start
        prev_was_non_word = False
        
        # We need to look back in the result list effectively by checking current index vs last added? 
        # Actually simpler: track if we just saw a whitespace character.
        
        # Re-evaluating logic for clarity without complex state tracking of history beyond one step:
        pass

    # Let's rewrite with clear single-pass logic
    
    final_chars = []
    
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        if not char.isspace():
            # Check if this is the start of a word (either beginning or after space/newline/tab)
            # We can infer "start of word" by checking if previous added characters ended with whitespace OR it's index 0
            
            # But we are building list, so check last element? 
            # Easier: keep track of whether the immediately preceding character in original string was non-word char.
            
            # Actually, simplest robust way without regex:
            # If current is not space and (i == 0 or text[i-1] is whitespace), then it's start of word.
            
            if i > 0 and text[i - 1].isspace():
                final_chars.append(char.upper() if char.isalpha() else char)
                prev_was_space = True # Mark we just processed a space? No, mark that next non-space is capitalized
                
        else:
            # It's whitespace. Add to result as-is (preserve spaces).
            # However, standard "capitalize first letter" usually collapses multiple spaces or keeps them. 
            # Let's keep original spacing structure but capitalize the very first char of each contiguous word block.
            
            final_chars.append(char)
        
        i += 1

    return ''.join(final_chars)

# Corrected and finalized optimized implementation below:
def capitalize_first_letter_only(text):
    """
    Returns a new string where only the first character of every word is capitalized.
    
    A "word" is defined as a contiguous sequence of non-whitespace characters. 
    The function capitalizes the first alphabetic letter found at the start of each such sequence.
    
    Time Complexity: O(n) - Single pass through the string.
    Space Complexity: O(n) - To store the result list (where n is length of input).
    
    Args:
        text (str): Input string with words separated by whitespace.
        
    Returns:
        str: Output string with capitalized first letters per word, preserving original spacing structure 
             except for ensuring exactly one capital at start of each non-whitespace block if applicable.
             
    Note: If the input has multiple spaces between words, they are preserved as in standard text processing unless specified otherwise.
         Only alphabetic characters are considered for 'capitalization' to avoid modifying digits/symbols which don't have case.
    """
    result = []
    
    # Flag to track if we need to capitalize the next non-whitespace character
    needs_capitalization = False
    
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        if not char.isspace():
            # Non-whitespace character encountered
            
            if needs_capitalization and 'a' <= char.lower() or ('A' <= char): 
                # If it's a letter, capitalize it; otherwise just keep as is (e.g., digits)
                result.append(char.upper())
                needs_capitalization = False  # Reset after handling start-of-word logic for this block? 
                                           # Wait, only the FIRST gets capitalized. Subsequent in same word stay original case.
            else:
                # If not a letter (like digit), we still need to track if it's START of word but don't change char value itself unless it is alpha.
                # Actually logic simplifies: 
                # 1. Is start of new block? -> Capitalize IF alphabetic.
                
                result.append(char)
            
            needs_capitalization = False
            
        else:
            # Whitespace character - preserves structure but resets the "start of word" flag for next non-space char
            if not (i == 0 and text[i-1].isspace()): 
                 # Actually simpler logic without looking back at original string index relative to result list complexity:
                pass
            
            # Correct reset logic using a boolean state that flips when we encounter whitespace followed by non-whitespace?
            # Let's use the 'needs_capitalization' flag correctly.
            
            needs_capitalization = True
        
        i += 1
    
    return ''.join(result)

# Final clean implementation for submission:

def capitalize_first_letter_only(text):
    """
    Returns a new string where only the first character of every word is capitalized.
    
    Efficient single-pass algorithm O(N).
    Preserves original whitespace structure (multiple spaces kept if present in input, 
    though typically such functions normalize to single space; here we preserve exact spacing layout relative to words).
    
    Only alphabetic characters are subject to capitalization rules at the start of a word.
    Digits and symbols appearing as first char will remain unchanged but still mark end-of-word for next block logic? 
    Actually, standard definition: "word" = sequence of letters/digits/underscores or just non-space chars?
    
    Given ambiguity in "character", we assume strictly alphabetic capitalization (A-Z -> A-Z).
    If input is "123 hello 456 world": Output should be "123 Hello 456 World".
    """
    result = []
    needs_capitalization = False
    
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]

if __name__ == '__main__':
    pass
