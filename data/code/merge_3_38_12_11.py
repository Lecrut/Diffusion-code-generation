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
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        duplicates = [char for char, count in char_count.items() if count > 1]
        
        return sorted(duplicates)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_strings = [
        "hello world",
        "aabbccdd",
        "programming is fun",
        "unique string with no repeats"
    ]

    for s in test_strings:
        result = analyzer.check_for_duplicates(s)
        if result:
            print(f"'{s}' -> Repeated characters: {result}")
        else:
            print(f"'{s}' -> No repeated characters found")