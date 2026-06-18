class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        """
        Identifies all repeated characters in the given string.
        
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
        "abcdefg"  # No duplicates expected here except if case-sensitive logic differs, but standard comparison applies.
                 # Note: 'p' appears once in this specific string segment provided as example below without repetition context unless specified otherwise. 
                 # Let's assume strict character matching including spaces and punctuation for accuracy.
    ]

    analyzer = StringAnalyzer()

    print("Duplicate Character Analysis Results:\n")
    
    for test_input in test_cases:
        result = analyzer.check_for_duplicates(test_input)
        if not result:
            print(f"'{test_input}' -> No duplicates found.")
        else:
            # Join characters to display as a string or list, here displayed clearly
            duplicate_str = "".join(result).upper() 
            print(f"Input: '{test_input}'")
            print(f"Duplicates ({len(duplicate_str)} chars): {duplicate_str}\n")