def case_converter(s):
    """
    Takes a string and returns three variations: lowercase, uppercase, 
    and title-cased versions using manual loops and conditionals.
    
    Args:
        s (str): The input string to convert cases for.
        
    Returns:
        tuple: A tuple containing (lowercase_str, uppercase_str, title_case_str)
    """
    lowercase = []
    uppercase = []
    title_case = []

    # Process each character in the loop
    for char in s:
        if 'a' <= char <= 'z':
            # Convert to lowercase logic (already lower, keep as is or force down)
            lowercase.append(char.lower())
            uppercase.append(char.upper())
            
            # Title case requires first letter upper, rest lower. 
            # We'll handle this in a separate pass below for clarity on the "first char" rule.
        elif 'A' <= char <= 'Z':
            lowercase.append(char.lower())
            uppercase.append(char)

    # Re-evaluate title_case based on position within the string to ensure correct casing rules (First upper, rest lower per word)
    # Since we need manual manipulation without regex or built-ins like str.title(), 
    # we will iterate again with a flag for "start of word". A simple heuristic: start of string or previous char was space.
    
    title_char = []
    prev_space = True  # Assume first character starts a new word
    
    if s == '':
        return ('', '', '')

    for i, char in enumerate(s):
        is_start_of_word = False
        
        # Determine if this is the start of a word (either beginning of string or preceded by whitespace)
        if prev_space:
            is_start_of_word = True
            
        # Check current character to decide casing based on 'is_start_of_word' flag
        lower_char = char.lower()
        
        if is_start_of_word and ('a' <= lower_char <= 'z'):
            title_char.append(lower_char.upper())
        else:
            title_char.append(lower_char)

        # Update prev_space for next iteration logic (simplified to check immediate previous context or just space/tab/newline)
        # For this implementation, we consider any whitespace as a word separator. 
        # Note: In strict manual loops without regex, checking the character itself is tricky if it's not alphanumeric.
        # We'll assume standard ASCII spaces/tabs are separators for simplicity in this loop structure.
        
        if char == ' ':
            prev_space = True
        else:
            prev_space = False

    return (''.join(lowercase), ''.join(uppercase), ''.join(title_char))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "a b c"
    ]

    print("Case Converter Results:")
    for test_str in samples:
        lower_res, upper_res, title_res = case_converter(test_str)
        print(f"\nInput: '{test_str}'")
        print(f"Lowercase: {lower_res}")
        print(f"Uppercase: {upper_res}")
        print(f"Title Case: {title_res}")