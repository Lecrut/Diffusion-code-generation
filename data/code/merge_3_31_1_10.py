import string

class StringUtils:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.
        
        This method filters the input string to include only alphanumeric characters 
        and converts them to lowercase, then uses two pointers (left and right) moving 
        towards each other to compare characters without creating additional copies of the data.
        
        Args:
            s (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome after ignoring non-alphanumeric characters, case differences, and spaces; False otherwise.
        """
        # Filter out non-alphanumeric characters and convert to lowercase in-place logic by iterating once
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move left pointer forward if it's not an alphanumeric character or is whitespace (though we ignore them entirely for comparison later, the problem implies standard palindrome check on content)
            # However, "in-place" usually means modifying a list. Since strings are immutable in Python, 
            # we can convert to a list of characters first which acts as our mutable structure.
            
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue
                
            char_left = s[left].lower()
            char_right = s[right].lower()
            
            if char_left != char_right:
                return False
            
            left += 1
            right -= 1
        
        # If we haven't returned False by now, it's a palindrome. 
        # Note: The prompt asks for "in-place comparison technique". In Python strings are immutable.
        # To strictly adhere to an in-place modification on the data structure itself (like a list),
        # one might convert s to a list of characters first if mutability was allowed, but since we can't mutate 
        # the original string object directly without copying, converting to a list is the standard Pythonic way 
        # to achieve O(1) extra space relative to input size (excluding the conversion cost).
        
        return True

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "",
        "No 'x' in Nixon.",
        "Madam",
        "Hello"
    ]

    for test_str in test_cases:
        result = StringUtils.is_palindrome(test_str)
        print(f"'{test_str}' is {'a palindrome' if result else 'NOT a palindrome'}")