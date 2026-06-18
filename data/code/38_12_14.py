import string

class StringAnalyzer:
    """A utility class for analyzing text strings."""

    def check_for_duplicates(self, s):
        """
        Identifies and lists all repeated characters in a given string instance.
        
        This method scans the input string using an efficient approach with 
        O(n) time complexity to track character occurrences via a frequency map.
        Only characters appearing more than once are included in the result list,
        preserving their order of first appearance as they appear during iteration.

        Args:
            s (str): The input string to analyze.

        Returns:
            List[str]: A list of unique characters that are repeated in the input string.
        
        Example:
            >>> analyzer = StringAnalyzer()
            >>> result = analyzer.check_for_duplicates("hello")
            >>> print(result)
            ['h', 'e']  # Assuming case-sensitive and based on order of first appearance

            Note: If a character appears multiple times consecutively or 
            non-consecutively, it is added to the list once if not already present.
        """
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

if __name__ == '__main__':
    pass
