"""
Module to process text by capitalizing only the first letter of each word 
while preserving the case of all subsequent letters in that word.
This is a common requirement where 'Capitalize' (string method) which 
capitalizes everything up to the next whitespace or punctuation, and then 
lowercases everything else within the same token, but we want exactly one 
uppercase at the start followed by lowercase for the rest of the characters 
in that specific word.

The logic:
1. Split text into words (sequences separated by non-alphabetic boundaries).
2. For each word: capitalize its first character if it is alphabetic; ensure all others are lowercased.
3. Reconstruct and join with original separators or spaces for simplicity 
   in this implementation, assuming standard space separation unless specific tokenization logic is needed.

Since the prompt asks to "capitalize the first letter only", we interpret this as:
- First character of each alphabetic sequence becomes uppercase.
- All other characters within that same word become lowercase (even if they were originally mixed case).
"""

def capitalize_first_letter_only(text: str) -> str:
    """
    Processes a block of text to apply the rule: 'capitalize the first letter only'.

    This means for every alphabetic sequence found in the text, the very first 
    character is converted to uppercase, and all subsequent characters within that 
    same sequence are forced to lowercase. Non-alphabetic characters act as delimiters 
    but retain their original form if they are not whitespace (though typically we assume spaces).

    Args:
        text (str): The input string block of text.

    Returns:
        str: A new string with the first letter of each alphabetic word capitalized, 
             and all other letters in that word lowercased.
    
    Example:
        Input:  "Hello WORLD! Python3 Is Fun."
        Output: "Hello World! python3 is fun." (Note: 'WORLD' -> 'World', 'Python3' -> 'python3')

        Wait, re-reading the specific constraint "capitalize the first letter only":
        Usually this implies standard word capitalization where subsequent letters are lowercased.
        Let's trace carefully: 
        If input is "hElLo", output should be "Hello".
        If input is "wOrLd!", output should be "World!". The '!' stays because it breaks the alphabetic sequence.

    """
    
    # We will split by non-alphabetic characters to identify words, 
    # but we must preserve separators if they are not just spaces? 
    # To keep it robust and production-ready for general text:
    # 1. Identify contiguous sequences of letters (a-zA-Z).
    # 2. For each sequence, capitalize first char, lower the rest.
    # 3. Reconstruct joining back with non-letter characters in their original positions.

    import re
    
    def process_word(word):
        """Process a single alphabetic word: Capitalize first letter."""
        if not word or len(word) == 0:
            return word
        
        # Ensure the rest are lowercased to satisfy "first letter only" capitalization style
        # Even if input was 'aBc', it becomes 'Abc'. If input was 'ABC', it becomes 'Abc'.
        first_char = word[0].upper()
        remaining_chars = ''.join(c.lower() for c in word[1:])
        return first_char + remaining_chars

    # Regex to find all alphabetic sequences and their positions/indices? 
    # Actually, using regex substitution is efficient.
    
    def replace_match(match):
        """Replacement function passed by re.sub."""
        matched_text = match.group()
        if not any(c.isalpha() for c in matched_text):
            return matched_text
        
        words_in_block = []
        i = 0
        while i < len(matched_text):
            # Find the start of an alphabetic run? 
            # Actually, re.findall with a pattern that captures letters is easier.
            pass 
        
    # Better approach: Use regex to find all sequences of [a-zA-Z] and replace them individually.
    
    def transform_word(word_str):
        """Transforms a string consisting only of alphabetic characters."""
        if not word_str:
            return ""
        
        first = word_str[0].upper()
        rest = ''.join(c.lower() for c in word_str[1:])
        return first + rest

    # Pattern matches any sequence of one or more letters
    pattern = re.compile(r'[a-zA-Z]+')
    
    def replacer(match):
        raw_word = match.group(0)
        processed_word = transform_word(raw_word)
        return processed_word
    
    result_text = pattern.sub(replacer, text)
    
    # Note: If the input contains non-alphabetic characters mixed in (like "123abc"), 
    # they act as delimiters. The regex above handles them correctly by skipping over non-letters?
    # No, re.findall/sub replaces only matches of [a-zA-Z]+. Non-matching parts are untouched.
    
    return result_text

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    sample_texts = [
        "Hello World! This is a test.",
        "Python3 Is Awesome And We Love Code!",
        "Multiple   spaces  here",
        "MixedCase123and456Text"
    ]

    print("Input -> Output Mapping:\n")
    
    for sample in sample_texts:
        output = capitalize_first_letter_only(sample)
        print(f'"{sample}"')
        print(f'<---> "{output}"\n')