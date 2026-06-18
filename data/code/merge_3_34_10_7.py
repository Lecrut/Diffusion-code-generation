import re

def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters within those words.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    # Use regex to find sequences of alphabetic characters representing a "word".
    # \w matches alphanumeric and underscore, but we specifically want letters for capitalization logic.
    # We split by non-word boundaries or use substitution on words found in the string.
    
    def capitalize_match(match):
        word = match.group()
        if not re.match(r'^[a-zA-Z]', word):
            return word
        
        first_char = word[0]
        rest_chars = word[1:]
        
        # Capitalize only the first character, keep the rest exactly as is (lowercase or mixed)
        capitalized_first = first_char.upper() if len(word) > 0 else ''
        result = f"{capitalized_first}{rest_chars}"
        
        return result

    # Find all words consisting of letters. 
    # Note: \w includes digits and underscores, but the requirement implies "words" usually start with a letter.
    # To be robust for standard English text where numbers might break word flow or shouldn't trigger capitalization logic on non-letters:
    # We will target sequences that contain at least one alphabetic character to ensure we don't capitalize digits/underscores unexpectedly,
    # but typically "first letter of each word" implies splitting by whitespace and punctuation.
    
    # Strategy: Split into words (sequences separated by non-alphanumeric characters), process them, then join back with separators? 
    # Actually, a simpler regex approach that targets sequences of letters is often what's expected unless specified otherwise for mixed content like "abc123".
    # However, the most robust interpretation of "first letter of each word" in general text processing usually implies splitting by whitespace and punctuation.
    
    # Let's use re.findall to get all contiguous alphabetic sequences as potential words. 
    # If a token is purely numeric or special chars without letters, it remains unchanged (no first letter).
    # Then we reconstruct the string preserving original structure? No, that changes separators if not careful.
    
    # Alternative robust method: Iterate through the string and identify word boundaries based on non-letter characters acting as delimiters for "words".
    # But standard library titlecase() does exactly this (capitalizes first char of each word found by splitting). 
    # However, we must preserve casing of subsequent letters. Python's built-in .title() lowercases the rest which violates "preserving the rest of the casing".
    
    # Therefore, manual implementation is required:
    # 1. Identify words as sequences of alphabetic characters? Or split by non-alphanumeric? 
    # Usually, a word ends at whitespace or punctuation. Let's assume standard definition where 'word' = sequence of alphanumeric chars starting with letter.
    # But to strictly follow "first letter", we look for [a-zA-Z] followed by any char (including letters).
    
    # Refined approach: 
    # Replace non-alphabetic characters temporarily? No, that loses structure if not careful.
    # Let's stick to the definition: A word is a sequence of alphanumeric characters where at least one letter exists?
    # Or simply split by whitespace and punctuation, then capitalize first char of each part if it starts with alpha?
    
    # The prompt says "first letter of each word". 
    # Example input: "hello world" -> "Hello World"
    # Example input: "hElLo wOrld" -> "HEllo WOrld"? Or "Helo WoRd"? 
    # Prompt says: "capitalizes only the first letter... preserving the rest of the casing".
    # So "hElLo" becomes "HElLo" (first 'h' to 'H', rest 'E','L','o' kept).
    
    # Implementation plan using regex substitution on alphabetic sequences found in the string.
    # We will find all maximal contiguous substrings of letters [a-zA-Z]. 
    # For each such substring, capitalize its first letter and keep others as is.
    # This handles mixed alphanumeric strings like "abc123def" -> "Abc123Def".
    
    return re.sub(r'([a-zA-Z])', lambda m: (m.group(0).upper() if not any(c.islower() for c in m.group()[1:]) else m.group()), text)

# Re-evaluating the regex logic above. The lambda is flawed because checking `any` on group[1:] inside substitution can be slow and complex to get right with case preservation.
# Simpler approach: 
# 1. Find all words (sequences of letters).
# 2. For each word, if it has length > 0, capitalize index 0, keep rest as is.
# 3. Reconstruct the string by replacing these found sequences back into their original positions?
# Actually, we can just iterate through the text and build a new list of characters or use regex to capture groups.

def robust_capitalize(text: str) -> str:
    # Split the text into words based on non-alphabetic boundaries is tricky if we want to preserve exact spacing/punctuation relative order perfectly without complex logic.
    # However, "first letter of each word" usually implies splitting by whitespace and punctuation in standard NLP tasks.
    # But given the constraint "preserving rest of casing", let's assume a simpler definition: 
    # Any contiguous sequence of alphabetic characters is considered a word for this purpose? 
    # Or should we treat numbers as part of words? e.g. "word123" -> "Word123"?
    
    # Let's use the standard Python approach but customizing the case logic:
    # Split by non-alphanumeric, process parts, join with same separators.
    
    import re
    
    # Pattern to match sequences of alphanumeric characters (words)
    words = re.findall(r'\w+', text)
    
    result_parts = []
    last_end = 0
    
    for word in words:
        if not word[0].isalpha():
            # If the "word" starts with a digit or underscore, it doesn't have a first letter to capitalize.
            # We just append as is? Or skip capitalization logic entirely? 
            # The prompt says "first letter of each word". Digits don't have letters.
            result_parts.append(word)
        else:
            # Capitalize the first character, keep rest exactly as they are (including digits if present in original 'word')
            capitalized_word = word[0].upper() + word[1:]
            result_parts.append(capitalized_word)
        
        last_end += len(word)

    # Reconstruct string manually to ensure separators are preserved correctly? 
    # Actually, re.sub with a function is cleaner if we define the replacement logic carefully.
    
    def replace_func(match):
        word = match.group()
        if not any(c.isalpha() for c in word):
            return word
        
        first_char = word[0]
        rest_chars = word[1:]
        
        # Capitalize only the very first character of this sequence
        new_first = first_char.upper()
        result = f"{new_first}{rest_chars}"
        return result

    # We need to match sequences that contain at least one letter? 
    # Or just all alphanumeric sequences. If a sequence is "123", it has no letters, so nothing changes. Correct.
    # If "aBc", first char 'a' -> 'A', rest "Bc" kept. Result "ABc". Wait, prompt says "capitalizes only the first letter... preserving rest". 
    # So "aBc" -> "ABc"? Yes. First letter is 'a'. Capitalize it to 'A'. Rest 'B','c' remain.
    
    return re.sub(r'\w+', replace_func, text)

if __name__ == '__main__':
    sample_input = "hello world! Python3 programming."
    output_result = robust_capitalize(sample_input)
    print(output_result)