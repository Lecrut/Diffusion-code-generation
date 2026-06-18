def case_converter(s):
    """
    Takes a string s and returns four versions of it: 
    - Lowercase (all characters lowercased)
    - Uppercase (all characters uppercased)
    - Title Case (First character of each word capitalized, the rest lowercase)

    The function manually processes characters using loops and conditionals.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        tuple: A tuple containing lower_case_str, upper_case_str, title_case_str
    """
    result_lower = ""
    result_upper = ""
    result_title = ""

    # Process for lowercase conversion using loop and conditionals (though not strictly necessary in Python)
    i = 0
    while i < len(s):
        char = s[i]
        
        if 'a' <= char <= 'z':
            result_lower += char.lower()
        elif 'A' <= char <= 'Z':
            # If already uppercase, keep as is or map explicitly. 
            # Explicit mapping for demonstration: A->a logic inside lower case block above covers it generally by .lower() but let's show manual check if we were not using built-in methods on the character itself directly to demonstrate manipulation principles requested in prompt implicitly
            result_lower += char.lower()  # This line executes regardless as per general Python behavior, manually mapping is redundant here without direct method call. The condition logic was for demonstration of "manipulating case" conceptually before .lower(). 
        else:
            result_lower += char
            
        i += 1

    # Process for uppercase conversion similarly with manual conditional checks and logic
    j = 0
    while j < len(s):
        char_u = s[j]

if __name__ == '__main__':
    pass
