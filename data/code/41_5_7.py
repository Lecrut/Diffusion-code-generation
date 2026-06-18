def case_converter(s):
    """
    Takes a string and returns three new strings: lowercase, uppercase, 
    and title-cased versions of the input using loops and conditionals.
    
    Args:
        s (str): The input string to convert cases for.
        
    Returns:
        tuple: A tuple containing (lowercase_str, uppercase_str, title_case_str)
    """
    lowercase = ""
    uppercase = ""
    title_case = []

    # Process each character in the original string using a loop and conditionals
    for char in s:
        if 'a' <= char <= 'z':  # Check if character is lowercase letter
            lower_char = char
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            title_case.append(upper_char if len(title_case) > 0 and title_case[-1].islower() else (char.upper() if not ' '.join([title_case[i] for i in range(len(title_case))]).strip().startswith(char.lower()) or char.isalpha() else lower_char))
        elif 'A' <= char <= 'Z':  # Check if character is uppercase letter
            upper_char = char
            lower_char = chr(ord(char) + ord('a') - ord('A'))
            title_case.append(lower_char if len(title_case) > 0 and title_case[-1].isupper() else (char.lower() if not ' '.join([title_case[i] for i in range(len(title_case))]).strip().startswith(char.upper()) or char.isalpha() else upper_char))
        elif char.isspace(): # Handle spaces correctly for Title Case logic manually
            title_case.append(' ')
            lower_char = ' '
            upper_char = ' '
        else:  # Non-alphabetic characters remain unchanged
            lower_char = char
            upper_char = char
        
        lowercase += lower_char
        uppercase += upper_char

    # Implement Title Case logic manually within the loop above for simplicity in this structure, 
    # but since we need to ensure proper title casing (first letter of each word capitalized),
    # let's re-implement the title case part more accurately based on words.
    
    # Re-calculate title_case properly: first char uppercase if alphabetic and not space, subsequent chars lowercase unless start of new word or non-alpha
    title_str = ""
    prev_space = True
    
    for i in range(len(s)):
        c = s[i]
        is_alpha = ('a' <= c <= 'z') or ('A' <= c <= 'Z')
        
        if not is_alpha:
            # Non-alphabetic characters are kept as is, but they act as word separators for title case logic? 
            # Standard Python title() treats non-letters like spaces. Let's mimic that behavior roughly.
            prev_space = True
            continue
            
        if i == 0 or s[i-1].isspace():
            # Start of a new "word" -> Capitalize it manually using conditional check against original char case
            if 'a' <= c <= 'z':
                title_char = chr(ord(c) - ord('a') + ord('A'))
            else:
                title_char = c
        elif prev_space and not ('a' <= s[i-1] <= 'z'): # If previous was space or non-alpha, treat as new word start? 
             # Actually standard behavior is based on whitespace. Let's stick to simple logic: capitalize if it follows a space/newline/non-word-char OR at start
            title_char = chr(ord(c) - ord('a') + ord('A'))
        else:
            # Middle of word -> lowercase
            title_char = c.lower()

        prev_space = False
        
    # Wait, the above manual logic inside the first loop was flawed. Let's do a clean pass for Title Case specifically below 
    # to ensure correctness without relying on external functions like .title().
    
    final_title_chars = []
    in_word = True
    
    for i, char in enumerate(s):
        is_alpha = ('a' <= char <= 'z') or ('A' <= char <= 'Z')
        
        if not is_alpha:
            # Non-alpha chars are added as-is. They break the word continuity? 
            # Python's title() behavior: "hello world" -> "Hello World". "hello-world" -> "Hello-World"? No, actually "Hello-World".
            # Actually standard title(): consecutive non-alphabetic characters don't separate words in a way that capitalizes them again unless they are whitespace.
            # Let's implement the most common expectation: capitalize first char of string and after any whitespace or sequence of non-alpha? 
            # Simpler approach for this task constraint "manual manipulation": Capitalize if it is alpha, not space, and (index==0 OR s[i-1] in ' \t\n\r' or i>0 and s[i-1].isalpha() == False).
            
            final_title_chars.append(char) # Keep non-alpha as is
            
        elif char.islower():
            if i == 0:
                final_title_chars.append(chr(ord(char) - ord('a') + ord('A')))
            else:
                prev_char = s[i-1]
                if not ('a' <= prev_char <= 'z') and not ('A' <= prev_char <= 'Z'): # Previous was non-alpha (like hyphen or number?) 
                    final_title_chars.append(chr(ord(char) - ord('a') + ord('A')))
                else:
                    final_title_chars.append(char.lower()) # Ensure lowercase if middle of word? No, just keep logic simple.
        elif char.isupper():
            if i == 0 or (not ('a' <= s[i-1] <= 'z')) and not ('A' <= s[i-1] <= 'Z'): 
                final_title_chars.append(char) # Keep uppercase at start of word
            else:
                final_title_chars.append(chr(ord(char) + ord('a') - ord('A')))

    title_str = "".join(final_title_chars)
    
    return lowercase, uppercase, title_str

if __name__ == '__main__':
    sample_strings = ["hello world", "HELLO WORLD", "hElLo WoRlD"]
    for test_input in sample_strings:
        lower_out, upper_out, title_out = case_converter(test_input)
        print(f"Input: '{test_input}'")
        print(f"Lowercase: '{lower_out}'")
        print(f"Uppercase: '{upper_out}'")
        print(f"Title Case: '{title_out}'")
        print("-" * 20)