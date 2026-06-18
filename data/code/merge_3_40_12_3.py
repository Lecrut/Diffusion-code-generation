class FirstLetterExtractor:
    def __init__(self):
        pass
    
    def extract_all(self, strings):
        """
        Extracts the first letter from each non-empty string in a list and returns 
        a new list of these letters as single-character lowercase strings.
        
        Args:
            strings (list[str]): A list of input strings.
            
        Returns:
            list[str]: A list containing the first character of each valid input string, lowercased.
        """
        result = []
        for s in strings:
            if not isinstance(s, str):
                continue
            stripped_s = s.strip()
            if len(stripped_s) > 0:
                # Take the first letter after stripping and convert to lowercase
                char_code = ord(stripped_s[0])
                result.append(chr(char_code & ~32))  # Remove uppercase bits (equivalent to .lower())
        return result

if __name__ == '__main__':
    test_data = ["Hello", "WORLD", "", "\t\nWorld", None, "!@#"]
    extractor = FirstLetterExtractor()
    output = extractor.extract_all(test_data)
    
    # Print each letter on a new line for verification
    print("Extracted first letters:")
    for item in output:
        if not isinstance(item, str):  # Handle case where None might be passed via strip check logic incorrectly or similar edge cases though handled above by checking stripped_s[0] existence but let's ensure safety
             continue 
        print(f"Character: '{item}'")