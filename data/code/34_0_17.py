import re

def capitalize_words(s: str) -> str:
    """
    Capitalizes the first letter of each word in the string,
    preserving the casing of the rest of the letters and non-alphabetic characters.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized.
    """
    # Use regex to find all words consisting of alphanumeric characters or underscores.
    # \b ensures we match whole words, [a-z] matches lowercase letters (assuming standard English input).
    # The replace function will use a callback to capitalize the matched groups.
    
    def cap_group(match):
        original = match.group(0)
        if len(original) == 1:
            return original.upper()
        
        first_char = original[0].upper()
        rest_chars = original[1:]
        
        # Check each character in the rest of the string to preserve existing casing logic.
        # We iterate through and build a list of characters, keeping the case as is for non-first letters.
        result_list = [first_char]
        remaining_part = " ".join(original.split())  # Ensure spaces between words are handled correctly
        
        # A more robust approach without regex replacement complexity:
        # Split by whitespace to get individual words, capitalize first letter of each word, then join back with space.
        
    return re.sub(r'[a-z]', lambda m: (m.group()[0].upper() if not any(c.islower() for c in ''.join(m.groups())) else m.group()), s)

def robust_capitalize_words(s: str):
    """
    Robust implementation to capitalize the first letter of each word.
    
    Steps:
    1. Split string into words based on whitespace (handles multiple spaces, tabs, etc.).
    2. For each non-empty word:
       - Capitalize its first character if it is alphabetic.
       - Keep subsequent characters exactly as they are in the original word.
    3. Join the processed words back with a single space to maintain structure and remove extra spaces if desired, 
       or preserve them by joining without an argument (default ' '). The problem asks for "each word", implying standard capitalization rules.
    
    Note: To strictly "preserve the rest of the casing" while only changing the first letter's case status from lowercase to uppercase (if it was a starting position), we assume 
          that if there is no existing upper/lower logic needed, just capitalize the first char found at index 0 and leave others alone.
          
    However, usually "capitalize word title case" implies: First letter Upper, rest Lowercase? No, task says "preserving the rest of the casing".
    So: Word -> 'wOrLd' becomes 'WoRlD'. Just change first char to upper if it's lower. If already upper or symbol, leave. 
         Wait, usually we expect input like "hello WORLD" -> "Hello World"? Or just ensure the FIRST letter is UPPERCASE regardless of original state?
         
    Let's re-read: "capitalizes only the first letter ... preserving the rest".
    
    Algorithm:
       For each word in split():
         If empty, skip.
         Take char at index 0 -> upper() (assuming it needs to be capitalized). 
            What if it is already uppercase? Upper() does nothing bad.
            What if it's a digit or symbol? The task implies 'letter'. We should probably only act on letters.
         
    Revised plan:
       Iterate over characters of the word starting from index 1, keep them as they are (preserve casing).
       Take char at index 0: if isalpha(), make it upper(). Else leave alone? Or just always upperify first alpha found? 
       
    Let's assume standard definition where we only touch alphabetic chars.
    
    Example "hello" -> "Hello".
    Example "hElLo" -> "HeLlO"? No, that changes casing of others if they are lower but not the target. Wait. 
       Task: "capitalizes ONLY the first letter ... preserving the rest".
       
    So for "hElLo": First is 'h'. Make it 'H'. Rest "ElLo" stays as is. Result: "HEllo"? No, result "HeLlo". 
           Original index 0 -> h (lower) -> H. Index 1->E(stays E). Index 2->L(stays L).
           
    Correct logic:
       word = list(word_str)
       if word and not word[0].isalpha(): # If first char is alpha, capitalize it. 
           pass
        
        Wait, simpler:
          res_list = []
          for i, ch in enumerate(s):
             if i == 0 and s[i-1] != ' ': # Start of a new sequence (word) AND current char is alphabetic?
                Actually simple split logic first.
    
    Final Strategy:
       Split by whitespace to isolate words. Capitalize the first character of each word (if it's alpha). Join with space.
       
    """
    if not s: return ""
    
    # Normalize separators to single spaces for clean output? 
    # Or preserve original spacing? "capitalizes only the first letter of each word". Usually implies standard formatting.
    # Let's split by \s+ (one or more whitespace) and then join with ' '. This is robust against multiple spaces collapsing into one, which is typical behavior unless strict preservation requested on structure beyond words. 
    # Given "efficient string manipulation", regex replace might be cleaner but list comprehension + join is very pythonic and fast for single pass per word.
    
    parts = re.split(r'\s+', s.strip())
    capitalized_parts = []
    
    for part in parts:
        if not part: continue
        
        # Capitalize first char if alphabetic, leave rest as is (preserve casing).
        new_part = ''
        
        # We only modify the very first character of this word to uppercase. 
        # The constraint "preserving the rest" means we do NOT change 'e' in 'elOre' -> keep 'l', 'E', 'o'.
        if part[0].isalpha():
            new_part = part[0].upper() + part[1:]
        else:
            # If first char is not alpha (like a number or symbol), do we capitalize? 
            # "first letter" implies alphabetic. So leave it alone.
            new_part = part
            
        capitalized_parts.append(new_part)
        
    return ' '.join(capitalized_parts).strip()

if __name__ == '__main__':
    sample_string1 = "hello World PYTHON pythonic CODE!"
    # Expected: Hello World Python Code! (Wait, preserving casing of rest means 
    # hello -> Hello, World -> World, PYTHON -> PYTHON? No. "capitalizes only the first letter". 
    # So 'P' in 'PYTHON' stays 'P'. Rest 'YTHON' preserved as is.
    # Result: Hello World Pythonic Code! (Wait "python" was lower case now P). 
    # Let's trace logic: 
    # 1. hello -> H + ello = Hello
    # 2. World -> W + orld = World
    # 3. PYTHON -> P + YTHON = PYthon? No, first letter becomes Upper (it is already upper). Rest preserved. Result: PYTHON.
    # But usually "capitalize" implies Title Case where rest are lower? 
    # Task says: "capitalizes ONLY the first letter ... preserving the rest". 
    # So if input is "hello", output "Hello". If input "HELLO world", output "HELLO World"? Or "Hello Word"?
    # Strictly reading: Change case of FIRST char to UPPERCASE. Do not touch others.
    
    test_cases = [
        ("hello WORLD", "Hello WORLD"), 
        ("hELLO wOrld", "HEllo WOrd") # Wait, first letter 'h' -> 'H'. Rest preserved? hElLo -> H + ElLo. Yes.
        , ("a b c 123 xyz", "A B C 123 XYZ"), 
    ]

    for inp, desc in test_cases:
        result = robust_capitalize_words(inp)
        print(f"Input: '{inp}'")
        # Note on output logic based on strict reading of prompt vs common sense.
        # Prompt says "capitalizes ONLY the first letter". It does NOT say convert rest to lower. 
        # So 'hELLO' -> 'H' + 'ELLO' = 'HELLO'. Only if it was lowercase at start?