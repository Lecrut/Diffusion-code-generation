class StringChecker:
    def check(self, text):
        """
        Determines if a given string is a palindrome, ignoring case, spaces, punctuation, 
        and other non-alphanumeric characters. Returns True or False.
        
        Parameters:
            text (str): The input string to be checked.
            
        Returns:
            bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
        """
        # Handle edge case of empty string explicitly for clarity though logic covers it too
        if not isinstance(text, str):
            return False
        
        # Filter to keep only alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in text if char.isalnum()]
        
        # Use two-pointer approach for efficient O(n) comparison without creating a new reversed string copy explicitly
        left, right = 0, len(filtered_chars) - 1
        
        while left < right:
            if filtered_chars[left] != filtered_chars[right]:
                return False
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    checker = StringChecker()
    
    # Sample test cases with hard-coded values, no user input required
    samples = [
        "A man a plan a canal Panama",
        "race car",
        "No 'x' in Nixon",
        "",                 # Empty string
        "Was it a car or a cat I saw?",
        "1234567890"       # Not a palindrome (digits)
    ]
    
    for sample_text in samples:
        result = checker.check(sample_text)