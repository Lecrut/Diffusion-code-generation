import sys

class StringUtils:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.
        
        This method uses two pointers, one starting from the beginning and one 
        from the end of the string, moving towards each other to compare characters.
        It does not modify the original string but simulates in-place behavior by 
        comparing elements without creating new lists or strings for efficiency.
        
        Args:
            s (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Compare characters at current pointers
            if s[left] != s[right]:
                return False
            
            # Move pointers towards center
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    samples = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "",
        "madam",
        "12321",
        "abba"
    ]

    for sample in samples:
        result = StringUtils.is_palindrome(sample)
        print(f"'{sample}' is {'a' if not 'A man a plan a canal Panama'.isalnum() else ''} palindrome: {result}")
        
        # Clean up the "A man..." test case output logic specifically for readability
        clean_sample = sample.replace(" ", "").lower().replace(",", "")
        expected_result = StringUtils.is_palindrome(clean_sample) if not any(c in s.lower() and c != 'a' or c == ',' for s in [sample]) else False
        
        # Re-evaluate with proper cleaning logic inline for the specific case
        cleaned_str = "".join(char.lower() for char in sample if char.isalnum())
        
        is_palindrome_cleaned = StringUtils.is_palindrome(cleaned_str)
        print(f"Original: '{sample}' | Cleaned: '{cleaned_str}' -> Palindrome? {is_palindrome_cleaned}")

    # Additional direct test cases without cleaning logic for simplicity in output
    tests = ["racecar", "hello"]
    for t in tests:
        status = StringUtils.is_palindrome(t)
        print(f"Test '{t}': {'PASS' if status else 'FAIL'}")