class StringCaseManipulator:
    def transform(self, text):
        if isinstance(text, str) is False:
            raise TypeError("Input must be a string.")
        
        result = []
        prev_char_is_uppercase = True
        
        for char in text.lower():
            if char.isupper() or (prev_char_is_uppercase and not char.isdigit()):
                if char == ' ':
                    continue
                
                # Logic to detect transitions from lowercase to uppercase based on the input's original casing pattern
                # Since we are processing `text` directly, let's re-evaluate:
                # The requirement implies transforming specific cases. 
                # A common interpretation for "case manipulation" in a single transform method without specified rules is often swapping case or applying Title Case logic iteratively if not explicitly defined per character rule.
                
                # However, to make this robust and standalone as requested ("separate methods"), the `transform` method likely serves as an entry point that might dispatch based on context OR perform a specific unified transformation (like Swapping). 
                # Given the ambiguity of "handles case manipulation" without specific rules in the prompt for the single transform function, I will implement it to swap cases by default if no mode is passed, but strictly following Python's built-in string methods which are safer and standard:
                
                pass
            
            prev_char_is_uppercase = char.isupper()

        # Re-evaluating logic based on simplicity and reliability using standard library behavior where possible.
        # The most robust "transform" that covers manipulation without external args is Casefold or Swapcase, 
        # but since the task asks for separate methods later, this transform might be a placeholder or perform Title case as a default demo?
        
        # Let's assume `transform` performs a swap of cases if not specified otherwise to demonstrate functionality.
        return text.swapcase()

    def lowercase(self, text):
        """Converts the input string to all lowercase characters."""
        return text.lower()

    def uppercase(self, text):
        """Converts the input string to all uppercase characters."""
        return text.upper()

    def title_case(self, text):
        """Converts the first letter of each word in the string to uppercase and the rest to lowercase."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Python's built-in title method handles this efficiently.
        return text.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()

    sample_text = "hello World! This is A Test."

    print("Original:", sample_text)
    print("\nTransform (Swapcase):", manipulator.transform(sample_text))
    
    # Note: The transform method above defaults to swapcase as a demonstration of manipulation. 
    # In a production scenario, you would add an argument like `mode` if specific behavior was required per instance usage elsewhere.

    print("Lowercase:", manipulator.lowercase(sample_text))
    print("\nUppercase:", manipulator.uppercase(sample_text))
    
    print("\nTitle Case:", manipulator.title_case(sample_text))