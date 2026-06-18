class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        """
        Identifies all characters that appear more than once in the input string.
        
        Args:
            input_string (str): The string to analyze for duplicate characters.
            
        Returns:
            list[str]: A sorted list of unique characters that are duplicated 
                      within the input string, preserving case sensitivity.
                      
        Example:
            >>> analyzer = StringAnalyzer()
            >>> result = analyzer.check_for_duplicates("hello")
            # Output will include 'h', 'e', 'l' (since they appear more than once)
        """
        char_count = {}
        
        # Count frequency of each character in the string
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Collect characters that appear more than once and sort them
        duplicates = [char for count, char in sorted(char_count.items()) if count > 1]
        
        return duplicates

if __name__ == '__main__':
    analyzer = StringAnalyzer()

    sample_strings = [
        "hello world",
        "aabbccdd",
        "programming is fun!",
        "unique string with no repeats"
    ]

    for test_input in sample_strings:
        duplicates = analyzer.check_for_duplicates(test_input)
        print(f"\nInput: '{test_input}'")
        if duplicates:
            print("Repeated characters:", ", ".join(duplicates))
        else:
            print("No repeated characters found.")