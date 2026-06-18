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
        
        # Collect characters that appear more than once, avoiding duplicates in the result list
        seen_duplicates = set()
        for char, count in char_count.items():
            if count > 1 and char not in seen_duplicates:
                duplicates.append(char)
                seen_duplicates.add(char)

        return sorted(duplicates)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_strings = [
        "hello world",
        "aabbccdd",
        "programming is fun",
        "no duplicates here"
    ]

    analyzer = StringAnalyzer()

    for text in test_strings:
        result = analyzer.check_for_duplicates(text)
        print(f"'{text}' -> {result}")