import sys

class StringUtils:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Checks if a given string is a palindrome using in-place comparison technique.
        
        This method converts the string to a list of characters (mutable), then uses 
        two pointers starting from opposite ends, moving towards the center and comparing 
        elements for equality. Non-alphabetic or non-numeric characters are ignored by skipping them during iteration.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome considering only alphanumeric characters, False otherwise.
        """
        # Convert string to list for in-place modification capability
        char_list = [c.lower() for c in s]  # Normalize case
        
        left = 0
        right = len(char_list) - 1

        while left < right:
            l_char = char_list[left] if char_list else None
            r_char = char_list[right] if char_list else None

            if not (l_char.isalnum() and r_char.isalnum()):
                # Skip non-alphanumeric characters from both sides if necessary, though the loop logic ensures alignment. 
                # However, to strictly follow "in-place comparison" on alphanumeric content:
                
                if not l_char.isdigit():
                    left += 1
                    continue
                elif not r_char.isdigit():
                    right -= 1
                    continue
                    
            if char_list[left] != '':
                 c_l = chr(char_list.pop(left)) # This doesn't work for mixed types directly in a way that keeps structure simple without full conversion.
                                    # Let's stick to the two-pointer logic on characters, but optimize by converting once.

if __name__ == '__main__':
    pass
