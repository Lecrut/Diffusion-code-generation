def case_converter(s):
    """
    Takes a string and returns three variations: lowercase, uppercase, 
    and title-cased versions using manual loops and conditionals.
    
    Args:
        s (str): The input string to convert.
        
    Returns:
        tuple: A tuple containing (lowercase_str, uppercase_str, title_case_str)
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    lowercase_list = []
    uppercase_list = []
    title_list = []

    for char in s:
        # Determine character properties manually using ord() and chr() logic
        is_alpha = False
        lower_ord = None
        upper_ord = None
        
        code = ord(char)
        
        if 'a' <= char <= 'z':
            is_alpha = True
            lower_ord = code - 32 # ASCII difference between uppercase and lowercase letters
            
            # For title case, we need to check position relative to previous character logic 
            # but since we are building lists sequentially without stateful context for "previous",
            # standard Python's capitalization rules apply: first char of string or after space.
            # We will implement a simple rule: capitalize if it's the start (index 0) 
            # or follows whitespace, otherwise lowercase in title case logic here?
            # Actually, let's stick to standard definition for Title Case:
            # Capitalize first letter of each word, rest lower.
            
        elif 'A' <= char <= 'Z':
            is_alpha = True
            
    # Re-implementing with proper state tracking within the loop for title case logic
    
    lowercase_list = []
    uppercase_list = []
    
    # Reset for a clean pass to build all lists correctly based on index/whitespace rules if needed, 
    # or just apply standard transformations per char.
    # To strictly follow "manual manipulation", we will do one pass that builds the logic.
    
    lower_res = ""
    upper_res = ""
    title_res = []

    for i, char in enumerate(s):
        code = ord(char)
        
        if 'a' <= char <= 'z':
            # Lowercase: keep as is
            lower_res += char
            
            # Uppercase: convert to upper equivalent manually (code - 32)
            upper_char_code = code - 32
            upper_res += chr(upper_char_code)
            
            # Title Case logic: 
            # If it's the first character OR if previous non-space char was not followed by space?
            # Standard rule: Capitalize if index==0 or s[i-1] is whitespace. Else lowercase.
            prev_is_space = (i > 0) and (s[i-1].isspace())
            
            if i == 0 or prev_is_space:
                upper_char_code_title = code - 32
                title_res.append(chr(upper_char_code_title))
                
                # Ensure the rest of the word is lowercase in Title Case? 
                # Actually, standard title case capitalizes the first letter and lowercases the rest.
                # So if this char was NOT capitalized (i.e., not start or after space), it should be lowercased for title case too.
            else:
                # It's a middle character of a word -> must be lowercase in Title Case
                upper_char_code_title = code - 32
                title_res.append(chr(upper_char_code_title))

        elif 'A' <= char <= 'Z':
            lower_res += chr(code + 32)
            
            # Uppercase: keep as is
            upper_res += char
            
            # Title Case logic for existing uppercase chars in middle of word -> must be lowercase
            prev_is_space = (i > 0) and (s[i-1].isspace())
            
            if i == 0 or prev_is_space:
                title_res.append(char)
            else:
                lower_char_code_title = code + 32
                title_res.append(chr(lower_char_code_title))

        elif char.isspace():
            # Whitespace handling for Title Case logic (previous check covers start of word after space)
            # Just pass through as is or ensure it doesn't break the flow? 
            # Usually spaces are kept in place.
            lower_res += char
            upper_res += char
            title_res.append(char)

        else:
            # Non-alphabetic characters (digits, symbols): keep unchanged for all cases usually
            lower_res += char
            upper_res += char
            title_res.append(char)

    return lowercase_list + "", uppercase_list + "", "".join(title_list)

# Corrected and simplified implementation to ensure correctness without complex state logic errors in the draft above.
def case_converter_v2(s):
    """
    Takes a string and returns three variations: lowercase, uppercase, 
    and title-cased versions using manual loops and conditionals.
    
    Args:
        s (str): The input string to convert.
        
    Returns:
        tuple: A tuple containing the lowercased string, uppercased string, and title-cased string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Initialize result strings/containers
    lowercase_str = []
    uppercase_str = []
    title_case_list = []

    for i in range(len(s)):
        char = s[i]
        
        # Check if character is alphabetic to decide conversion logic
        ord_val = ord(char)
        is_lower_a_z = 'a' <= char <= 'z'
        is_upper_A_Z = 'A' <= char <= 'Z'

        # 1. Lowercase Logic: Always convert uppercase to lowercase, keep lower as is.
        if is_upper_A_Z:
            new_ord = ord_val - 32
            lowercase_str.append(chr(new_ord))
        else:
            lowercase_str.append(char)

        # 2. Uppercase Logic: Convert lowercase to uppercase, keep upper as is.
        if is_lower_a_z:
            new_ord = ord_val + 32
            uppercase_str.append(chr(new_ord))
        else:
            uppercase_str.append(char)

        # 3. Title Case Logic: 
        # Rule: Capitalize the first character of each word, lowercase all others in that word.
        # A "word" starts at index 0 or after a whitespace character.
        
        if is_lower_a_z:
            prev_char = s[i-1] if i > 0 else ''
            
            # Check if this char should be capitalized (start of string or start of new word)
            if i == 0 or not prev_char.isalpha() and not prev_char.isdigit(): 
                # It's the start of a "word" -> Capitalize it manually
                new_ord = ord_val + 32
                title_case_list.append(chr(new_ord))
                
                # Note: We don't need to force lowercase here because we are processing char by char.
                # The next chars will be handled in their own iterations based on the rule "not start of word".
            else:
                # It's a middle/end character -> Lowercase it manually (even if currently uppercase)
                new_ord = ord_val - 32
                title_case_list.append(chr(new_ord))
        elif is_upper_A_Z:
            prev_char = s[i-1] if i > 0 else ''
            
            # If current char is already upper, check if it should be lowercased (middle of word)
            if not (i == 0 or not prev_char.isalpha() and not prev_char.isdigit()):
                new_ord = ord_val + 32
                title_case_list.append(chr(new_ord))
            else:
                # Start of word -> Keep as uppercase
                title_case_list.append(char)
        elif char.isspace():
            # Spaces are preserved in their position, they don't affect case conversion logic directly 
            # other than marking the start of a new "word" for subsequent chars (handled by i==0 or prev check).
            title_case_list.append(char)
            
    return "".join(lowercase_str), "".join(uppercase_str), "".join(title_case_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    samples = [
        "Hello World",
        "Python 3.10",
        "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
    ]

    print("Input: 'Hello World'")
    lower, upper, title = case_converter_v