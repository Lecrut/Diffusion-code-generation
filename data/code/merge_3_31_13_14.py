class StringChecker:
    """A class to check if a string is a palindrome."""

    def check(self, text):
        """
        Determines if the input string is a palindrome.
        
        Handles edge cases like empty strings and mixed casing by converting
        all characters to lowercase before comparison. Non-alphanumeric characters are ignored? 
        NOTE: The prompt says "strings containing mixed casing", implying case-insensitivity matters,
        but does not explicitly state ignoring non-alphanumeric chars (like punctuation or spaces).
        Standard palindrome definition usually considers the exact sequence of characters provided,
        adjusted for case sensitivity. To be robust and follow typical "case-insensitive" patterns without 
        altering string structure (which might be unintended), we will convert to lowercase but keep all characters.
        
        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Handle empty strings as palindromes by definition
        if not text:
            return True
        
        # Convert to lowercase for case-insensitive comparison
        normalized_text = "".join(c.lower() for c in text)
        
        # Use two-pointer approach for efficiency (O(n))
        left, right = 0, len(normalized_text) - 1
        
        while left < right:
            if normalized_text[left] != normalized_text[right]:
                return False
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    
    checker = StringChecker()
    
    test_cases = [
        ("", "Empty string"),
        ("A man a plan a canal Panama!", "Sentence with mixed casing and punctuation (treated as exact sequence)"),
        ("racecar", "Simple palindrome"),
        ("hello world", "Not a palindrome"),
        ("No 'x' in Nixon.", "Palindrome with spaces, quotes, periods; case insensitive"),
    ]

    print("Running StringChecker tests...\n")
    
    for text, description in test_cases:
        result = checker.check(text)
        status = "Is Palindrome" if result else ("Not a palindrome (case-insensitive exact match)")
        
        # Note on punctuation/spaces: 
        # Since the task didn't specify filtering non-alphanumeric chars, we compare full normalized string.
        # 'No x in Nixon.' -> lowercase is same forwards/backwards? No: d!=e at end vs start?
        # Let's trace "racecar" -> r,a,c,e,c,a,r (palindrome)
        # "A man a plan a canal Panama!" -> lower, all chars included. 
        # '!' != 'a' => False unless we strip non-alpha. 
        # Given the ambiguity in prompt ("mixed casing"), assuming strict character sequence is safer than guessing filters.
        
        print(f"Test: '{text}'")
        print(f"Description: {description}")
        print(f"Result: {status}\n")