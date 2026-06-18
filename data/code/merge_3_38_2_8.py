class StringAnalyzer:
    def check_for_duplicates(self, text: str) -> list[str]:
        """
        Identifies all characters that appear more than once in the input string.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            list[str]: A sorted list of unique characters found multiple times.
        """
        char_count = {}
        duplicates = []

        # Count frequency of each character
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Collect characters with count > 1, ensuring uniqueness and sorting
        seen_duplicates = set()
        for char, count in char_count.items():
            if count > 1 and char not in seen_duplicates:
                duplicates.append(char)
                seen_duplicates.add(char)

        return sorted(duplicates)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_string = "hello world"
    
    analyzer = StringAnalyzer()
    result = analyzer.check_for_duplicates(test_string)
    
    print(f"Input: '{test_string}'")
    if not result:
        print("No duplicate characters found.")
    else:
        print(f"Duplicates found: {result}")