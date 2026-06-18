class StringAnalyzer:
    """A class to analyze strings for specific patterns."""

    def check_for_duplicates(self, input_string):
        """
        Identifies all characters that appear more than once in the given string.
        
        Args:
            input_string (str): The string to be analyzed.
            
        Returns:
            list: A sorted list of unique characters that are duplicated in the input string.
                  If no duplicates exist, returns an empty list.
        """
        char_count = {}
        duplicate_chars = set()

        # Count frequency of each character
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Identify duplicates based on count > 1 and add to a sorted list
        duplicate_chars_list = []
        
        for char, count in char_count.items():
            if count > 1:
                duplicate_chars_list.append(char)

        return sorted(duplicate_chars_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_string = "hello world"
    
    analyzer = StringAnalyzer()
    result = analyzer.check_for_duplicates(test_string)

    print(f"Input: '{test_string}'")
    print("Repeated characters:", result)