def case_converter(s):
    """
    Takes a string and returns three versions: lowercase, uppercase, and title-case.
    Uses loops and conditional logic to manually manipulate each character.
    
    Args:
        s (str): The input string
        
    Returns:
        tuple: A tuple containing (lowercase_str, uppercase_str, title_case_str)
    """
    # Initialize result lists for the three cases
    lower_chars = []
    upper_chars = []
    title_chars = []
    
    # Iterate through each character in the input string
    for char in s:
        # Determine if the character is alphabetic to handle case conversion logic
        if 'a' <= char <= 'z':
            # Lowercase logic: keep as is (or convert from uppercase to lowercase)
            lower_chars.append(char.lower())
            
            # Uppercase logic: convert to uppercase using conditional check on ASCII value or .upper() method simulation via ord/chr
            if 'A' <= char.upper() <= 'Z':
                upper_chars.append(''.join(chr(ord(c) - 32) for c in [char])[-1] if len(char) > 0 else '') 
                # Simulated manual uppercase: subtract 32 from ASCII value of lowercase to get uppercase equivalent
            else:
                upper_chars.append(char.upper())
                
        elif 'A' <= char <= 'Z':
            lower_chars.append(''.join(chr(ord(c) + 32) for c in [char])[-1] if len(char) > 0 else '') 
            # Simulated manual lowercase: add 32 to ASCII value of uppercase to get lowercase equivalent
            
            upper_chars.append(char.upper())
            
        elif char.isalpha():
            # Handle other alphabetic characters (e.g., non-English letters, though Python's string methods handle this)
            lower_chars.append(''.join(chr(ord(c)) for c in [char])[-1] if len(char) > 0 else '')
            upper_chars.append(''.join(chr(ord(c)) + 32 if ord(c) >= 65 and ord(c) <= 90 else '' for c in [char])[-1] if len(char) > 0 else '')

        # Title case logic: First letter uppercase, rest lowercase
        elif char.isalpha():
            first_char = True
            title_chars.append(''.join(chr(ord(c)) - 32 if ord(char) >= 97 and ord(char) <= 122 else chr(ord(char)) + 32 for c in [char])[-1] if len(char) > 0 else '')

    # If the above manual ASCII manipulation is getting complex, simplify using direct conditional checks on range
    lower_chars = []
    upper_chars = []
    title_chars = []
    
    new_lower = ""
    new_upper = ""
    new_title = ""
    
    for char in s:
        if 'a' <= char <= 'z':
            new_lower += char.lower()
            # Manual uppercase conversion from lowercase range to upper case equivalent (ASCII)
            new_upper += chr(ord(char.upper())) 
            first_char = True
            
        elif 'A' <= char <= 'Z':
            new_lower += chr(ord(char)) + 32 # Add 32 to convert Uppercase ASCII to Lowercase ASCII
            new_upper += char.upper()
            
    for i, char in enumerate(s):
        if not s[i].isalpha(): continue
        
        is_first = (i == 0) or not s[i-1].islower() and not s[i-1].isspace() 
        # More robust title case logic: capitalize first letter of string unless it's part of a word after space/punctuation

if __name__ == '__main__':
    pass
