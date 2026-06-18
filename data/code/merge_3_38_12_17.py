class StringAnalyzer:
    def check_for_duplicates(self, text):
        """
        Identifies all repeated characters in a given string instance.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            list[str]: A sorted list of unique characters that appear more than once in the string.
        """
        char_count = {}
        duplicates = []

        # Count frequency of each character
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Collect characters that appear more than once, avoiding redundant entries during collection by checking against a set before adding to list or using dict keys directly since we iterate over unique chars anyway. 
        # Actually iterating over the dictionary items ensures uniqueness per character type immediately.
        for char in char_count:
            if char_count[char] > 1:
                duplicates.append(char)

        return sorted(duplicates)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Hard-coded sample values as required (no user input, stdin, or args)
    test_strings = [
        "hello world",
        "aabbccdd",
        "programming is fun!",
        "abcdef"  # No duplicates expected here
    ]

    for s in test_strings:
        result = analyzer.check_for_duplicates(s)
        print(f"'{s}' -> {result}")