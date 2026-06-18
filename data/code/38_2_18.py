class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        """
        Identifies all repeated characters in a given string.
        
        Args:
            input_string (str): The string to analyze.
            
        Returns:
            list[str]: A sorted list of unique characters that appear more than once.
        """
        char_count = {}
        duplicates = []

        # Count frequency of each character
        for char in input_string:
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
    test_cases = [
        "hello world",
        "aabbccdd",
        "programming is fun",
        "abcdefg"  # No duplicates expected here (case-sensitive)
    ]

    analyzer = StringAnalyzer()

    for test_input in test_cases:
        result = analyzer.check_for_duplicates(test_input)
        print(f"Input: '{test_input}'")
        if result:
            print("Repeated characters:", ", ".join(result))
        else:
            print("No repeated characters found.")
        print("-" * 30)