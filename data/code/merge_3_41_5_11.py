def case_converter(s):
    """
    Takes a string `s` and returns three new strings: lowercase, uppercase, 
    and title-cased versions of the input using loops and conditional logic.
    
    Args:
        s (str): The input string to convert cases for.
        
    Returns:
        tuple: A tuple containing (lowercase_string, uppercase_string, title_case_string)
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    lowercase_result = ""
    uppercase_result = ""
    title_case_result = ""

    # Process each character for lowercase and uppercase conversion
    for char in s:
        is_upper_char = 'A' <= char <= 'Z'
        
        if is_upper_char:
            lower_code = ord(char) + 32
            upper_code = ord(char) - 32
            
            # Append to results based on logic
            lowercase_result += chr(lower_code)
            uppercase_result += char

    # Generate title case manually by checking each character's context
    for idx, char in enumerate(s):
        is_upper_char = 'A' <= char <= 'Z'
        
        if not is_upper_char:
            next_is_alpha = False
            
            # Check boundaries or non-alphabetic characters to determine start of title case word
            if idx == 0:
                next_is_alpha = True
            elif s[idx+1] and ('a' <= s[idx+1] <= 'z'):
                next_is_alpha = True
                
        else:
            # If it's uppercase, check previous char to decide whether it should be lowercase in title case
            if idx == 0 or not (('A' <= s[max(0,idx-1)] < 'Z') and ('a' <= s[min(len(s)-1,idx-1)] > None)): 
                pass # It starts a word, keep as is
            
        # Re-evaluate logic for strict manual title case:
        # First char of string or after non-alpha -> convert to upper if alpha
        # Otherwise -> lower unless it's the start of a new "word" in title context (which we handled above)
        
    # Let's re-implement the loop clearly inside this function block for correctness:

    lowercase_result = ""
    uppercase_result = ""
    
    # Clear previous logic attempts and do it correctly with one pass per case type or combined
    
    temp_lower = []
    temp_upper = []
    temp_title_words_start = False # Flag to track if we are at the start of a word for title case

    for char in s:
        code = ord(char)
        
        is_alpha = ('a' <= char <= 'z') or ('A' <= char <= 'Z')
        
        # Lowercase Logic

if __name__ == '__main__':
    pass
