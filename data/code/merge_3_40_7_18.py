class StringProcessor:
    """A utility class for processing string data."""

    def get_first_letter(self, text):
        """
        Returns the first letter of the very first word in the given string.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str or None: The first character of the first alphabetic 
                         word found, or None if no such word exists.
                         
        Raises:
            TypeError: If the input is not a string.
        """
        # Validate input type immediately for clarity and safety
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        # Split by whitespace to get words; strip handles leading/trailing spaces automatically
        words = text.split()
        
        # Check if the list is empty (empty string or only whitespace)
        if not words:
            return None
            
        first_word = words[0]
        
        # Iterate through characters of the first word to find the first letter
        for char in first_word:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                return char
        
        # If no alphabetic character is found (e.g., input was "123" or "!@#")
        return None

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    test_cases = [
        ("Hello World", 'H'),
        ("  Python Programming ", 'P'),
        ("   ", None),           # Only whitespace
        ("12345 Start Now", 'S'),  # Numbers before word
        ("!!! No Letters Here !!!", None),  # Non-alphabetic first char only in words
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", 'a')
    ]

    processor = StringProcessor()

    print("Testing get_first_letter method:\n")
    
    for input_str, expected in test_cases:
        result = processor.get_first_letter(input_str)
        
        # Determine status message based on match or mismatch
        if result == expected:
            status = "PASS"
        else:
            status = f"FAIL (Expected {expected}, got {result})"
            
        print(f'Input: "{input_str}"')
        print(f'Result: "{result}" | Status: {status}\n')