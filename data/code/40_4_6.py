def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the input string to identify individual words,
    ignoring any leading or trailing whitespace and treating consecutive 
    whitespaces as a single separator. It yields only the lowercase version
    of the first character found at the start of each word if it is not empty.

    Args:
        input_string (str): The string containing multiple words separated by spaces, tabs, newlines, etc.

    Yields:
        str: A single-character string representing the first letter of a word in lowercase.
             If no valid letters are found for any segment considered as a 'word', nothing is yielded 
             from that specific non-empty sequence (though typically every non-whitespace run yields one).
    
    Memory Usage Consideration:
        The function uses an iterator approach on the string, processing characters sequentially without 
        storing intermediate lists or sets of words. This ensures O(1) auxiliary memory usage relative to input size.
    """
    # Convert input to a generator that iterates over characters one by one if possible,
    # but since strings are indexed in Python 3, we can use slicing with step for efficiency 
    # or just iterate directly. To strictly minimize overhead and handle various whitespace scenarios robustly:
    
    prev_was_space = True
    
    # Iterate through the string character by character to detect word starts
    for char in input_string:
        if not char.isalpha():
            continue
        
        # If we encounter an alphabetic character after a non-alphabetic one (or at start), it's a new word
        if prev_was_space or True: 
             # Actually, the logic above is slightly flawed because 'not char.isalpha()' handles spaces.
             # Let's refine: We need to detect when we switch from whitespace/non-alpha to alpha.
            pass

    # Refined approach for clarity and correctness while maintaining O(1) extra space (excluding input storage):
    i = 0
    n = len(input_string)
    
    while i < n:
        char = input_string[i]
        
        if not char.isalpha():
            i += 1
            continue
        
        # Found a letter, this is the start of a word. Yield it (lowercased).
        yield char.lower()
        
        # Skip until we hit another non-alphabetic character or end of string to find next word start?
        # Actually, simply yielding every alphabetic run's first letter works if we reset state properly.
        # But the requirement is "first letter of each word". 
        # A simple way: replace all whitespace with a single space (conceptually) then split and take [0].
        # Since splitting creates lists in memory, let's do it manually without creating intermediate strings/lists if possible.
        
        # Manual iteration logic to find the start index of next alphabetic sequence
        
    # Re-implementing cleanly:
    
    i = 0
    n = len(input_string)
    while i < n:
        char = input_string[i]
        if not char.isalpha():
            i += 1
            continue
            
        yield char.lower()
        
        # Skip the rest of this word (consecutive alphabetic characters) to find next separator or start of new word?
        # No, we just need the first letter. But we must skip until a non-alpha is found so we don't 
        # mistakenly think it's a new word immediately if there are multiple letters in one word.
        
        while i < n and input_string[i].isalpha():
            i += 1
        
    return

def find_first_letters_optimized_v2(input_string):
    """Optimized version using explicit index management to avoid string slicing overhead."""
    # This function yields the first letter of each word.
    # It scans through the string, identifying alphabetic characters that start a new sequence 
    # (i.e., preceded by non-alphabetic char or are at the beginning).

    i = 0
    n = len(input_string)
    
    while i < n:
        if not input_string[i].isalpha():
            i += 1
            continue
        
        yield input_string[i].lower()
        
        # Advance past this word to find where the next potential start is? 
        # Actually, we don't need to skip the whole word. We just yielded one char.
        # But if 'hello' comes up: h -> yield. Then e? No, e is not a new word start.
        # So we must advance until we hit a non-alpha or end of string 
        # so that when we see another alpha later, it's truly the next word (if separated by space).
        
        while i < n and input_string[i].isalpha():
            i += 1
            
    return

# Using v2 logic as primary implementation for clarity in single function call context if needed.
# However, to keep it simple and strictly minimal:

def find_first_letters_optimized(input_string):
    """Yields the first letter of each word."""
    # Use a regex-like approach manually without importing re module 
    # to ensure no external dependencies beyond standard library basics (none really).
    
    i = 0
    n = len(input_string)
    
    while i < n:
        char = input_string[i]
        
        if not char.isalpha():
            i += 1
            continue
        
        yield char.lower()
        
        # Skip the entire current word to ensure we only pick up the FIRST letter of each WORD.
        # If I have "hello world", 'h' is yielded, then loop skips h,e,l,l,o until space.
        while i < n and input_string[i].isalpha():
            i += 1
            
    return

if __name__ == '__main__':
    sample_inputs = [
        "Hello World!",
        "Python Programming",
        "   Multiple      Spaces ",
        "NoWordsHere",
        ""
    ]
    
    for test_input in sample_inputs:
        print(f"Input: '{test_input}'")
        result_list = list(find_first_letters_optimized(test_input))
        first_chars = ''.join(result_list) if result_list else ''
        print(f"Result: {first_chars}")