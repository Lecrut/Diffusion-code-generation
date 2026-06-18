def case_converter(s):
    """
    Takes a string s and returns three new strings:
    1. Lowercase version of s (if any lowercase characters exist)
    2. Uppercase version of s (if any uppercase characters exist)
    3. Title-cased version of the original string
    
    The function uses loops and conditional logic to manually manipulate case,
    without using built-in str methods like .lower(), .upper() or .title().
    
    Args:
        s (str): Input string
        
    Returns:
        tuple: A tuple containing three strings in order of lowercase, uppercase, titlecase.
               If the input is empty or only contains non-alphabetic characters, 
               all returned values will be empty strings except possibly for a mixed case check logic.
    
    Logic:
        - Iterate through each character to determine its current state (alpha/non-alpha).
        - Build lowercase string by converting alpha chars if they are uppercase.
        - Build uppercase string by converting alpha chars if they are lowercase or non-alphabetic but not space? 
          Actually, the problem says "lowercase, uppercase and title-cased". Title case implies capitalizing first char of each word.
    """

    # Helper function to check for alphabets (A-Z, a-z) using ASCII logic manually if needed, though ord() is allowed as it's built-in but not str method. 
    def is_alpha(char):
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z')

    # Initialize result strings with placeholders to handle empty input gracefully later? Or just process normally and append if non-alphabetic chars encountered (but we must not use str methods). 
    lowercase = ''  # Placeholder for lowercased string
    uppercase = ''   # Placeholder for uppercased string
    
    title_case_str = s[0] + ' ' * len(s) - 1 # Initialize with first char and spaces as placeholder until fully processed

    if not is_alpha(title_case_str): 
        return '', '', ''

    i=0

if __name__ == '__main__':
    pass
