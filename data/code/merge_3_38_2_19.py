class StringAnalyzer:
    def check_for_duplicates(self, text: str) -> list[str]:
        """
        Identifies all characters that appear more than once in the input string.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            List of unique characters found as duplicates. Order is preserved 
            based on their first appearance, but only includes those with count > 1.
        """
        char_count = {}
        duplicate_chars = []

        for char in text:
            if char not in char_count:
                # Only track order of first occurrence here to maintain consistency
                pass
            
            char_count[char] += 1
        
        # Iterate through the original string again to preserve relative order 
        # and only add characters that are actually duplicated.
        for char in text:
            if char_count[char] > 1 and (not duplicate_chars or duplicate_chars[-1] != char):
                duplicate_chars.append(char)

        return duplicate_chars

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_string = "hello world"
    
    analyzer = StringAnalyzer()
    result = analyzer.check_for_duplicates(test_string)

    print(f"Input: '{test_string}'")
    print("Repeated characters found:", result)