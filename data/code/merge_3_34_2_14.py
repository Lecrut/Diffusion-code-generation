class StringCapitalizer:
    """A class to capitalize specific parts of a string."""

    def capitalize_words(self, input_string):
        """
        Capitalizes only the first letter of each word in the given string.

        Args:
            input_string (str): The string to process. Words are defined as sequences 
                               separated by whitespace or punctuation that acts as a delimiter 
                               between words for this purpose. Non-alphabetic characters do not 
                               get capitalized unless they start a new 'word' segment in the context 
                               of alphabetic transitions, but primarily we focus on standard word boundaries.
        
        Returns:
            str: A new string with the first letter of each word capitalized.

        Example:
            >>> sc = StringCapitalizer()
            >>> result = sc.capitalize_words("hello world")
            >>> print(result)
            "Hello World"
        """
        if not input_string or not isinstance(input_string, str):
            return ""

        # Split the string into words based on whitespace and simple punctuation 
        # to handle cases like "hello-world" -> ["hello", "world"] effectively.
        import re
        
        # Use regex to split by non-alphabetic characters that act as separators between words
        # This handles spaces, tabs, newlines, hyphens, underscores (treated as word boundaries here for simplicity)
        tokens = re.split(r'(?<=[a-zA-Z])(?![a-zA-Z])|[^a-zA-Z]+', input_string.strip())

        result_parts = []
        
        # Iterate through each token found by the split logic. 
        # We need to reconstruct the string carefully because simple splitting might lose structure if not careful.
        # A more robust approach for "first letter of each word" usually implies standard whitespace separation,
        # but let's handle punctuation as separators too while keeping original spacing where possible?
        # Actually, a simpler and common interpretation: split by any non-letter sequence, capitalize first char 
        # if it exists in the token (if we treat tokens as words), then join. But this loses spaces/punctuation positions.
        
        # Let's use a regex findall to identify word boundaries or simply iterate characters?
        # Standard approach for "first letter of each word": split by whitespace, capitalize first char of each part, join with space.
        # However, the prompt implies general words. 
        # Let's stick to: Split by any non-alphabetic character sequence that separates letters.
        
        # Refined strategy using regex substitution or findall logic on a cleaner basis:
        # Find all sequences of alphabetic characters. Capitalize their first letter if they are not empty.
        # Then reconstruct the string preserving original structure? 
        # Or just standard "words" separated by whitespace/punctuation?
        
        # Let's assume 'word' is defined as a contiguous sequence of letters [a-zA-Z].
        matches = re.findall(r'[a-zA-Z]+', input_string)
        
        if not matches:
            return input_string

        capitalized_matches = []
        for match in matches:
            if len(match) > 0 and (match[0] == 'A' or match[0].isupper()):
                # Already starts with uppercase, keep as is? 
                # Usually "capitalize" means ensure it's upper. If already upper, no change needed to first char logic usually implies making it Upper if lower.
                # But strictly: capitalize the letter itself (make it upper).
                capitalized_matches.append(match[0].upper() + match[1:])
            else:
                capitalized_matches.append(match)

        # Now we need to map these back to positions in the original string? 
        # That's complex. A simpler, standard interpretation for such tasks is often just splitting by whitespace and punctuation, capitalizing first letter of parts, then joining with a space or similar.
        # BUT, if I change spaces/punctuation, it might violate "input" fidelity unless specified to normalize output format.
        
        # Let's try the most robust method: Replace non-alphabetic chars temporarily? No.
        # Alternative: Use regex replace. 
        # Pattern: Find a letter that is preceded by either start of string or a non-letter character (and not part of an existing uppercase sequence if we want strict 'first').
        
        def capitalize_first_letter(match):
            return match.group(0).upper()

        # Regex explanation: (?<=\s|(?<=[a-zA-Z])) - wait, that's for start.
        # We want to find a letter [a-z] or [A-Za-z]. 
        # If it is the first character of a word (preceded by non-letter or string start), capitalize it.
        
        result = re.sub(r'(?<=[^a-zA-Z]|^)([a-zA-Z])', lambda m: m.group(1).upper(), input_string)

        return result

if __name__ == '__main__':
    # Hard-coded sample values to test the class functionality without user input.
    
    tester = StringCapitalizer()
    
    samples = [
        "hello world",
        "python programming is fun!",
        "  multiple   spaces ",
        "one-two-three-four-five",
        "already Capitalized",
        "",
        "no letters here 12345"
    ]

    print("Testing StringCapitalizer.capitalize_words()")
    for sample in samples:
        output = tester.capitalize_words(sample)
        print(f'Input : "{sample}"')
        print(f'Output: "{output}"\n')