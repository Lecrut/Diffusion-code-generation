class StringAnalyzer:
    def __init__(self):
        """Initialize the StringAnalyzer class."""
        pass
    
    def check_for_duplicates(self, text: str) -> list:
        """
        Identify and return a list of all characters that appear more than once in the input string.
        
        Args:
            text (str): The string to analyze for duplicate characters.
            
        Returns:
            list: A sorted list of unique character strings that are duplicates.
                  If no duplicates exist, returns an empty list.
        """
        char_count = {}
        duplicates = set()
        
        # Iterate over each character in the text and count occurrences
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
            # If a character's count exceeds 1, add it to the duplicates set immediately.
            # This ensures O(1) check time per iteration.
            if char_count[char] > 1:
                duplicates.add(char)
        
        return sorted(list(duplicates))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    analyzer = StringAnalyzer()
    
    test_cases = [
        "hello world",      # Expected duplicate: 'l' (or ['h', 'w'] depending on implementation, but here 'l') -> actually l and o? h,e,l,l,o,w,o,r,l,d. Wait: h=1, e=1, l=3, o=2, w=1, r=1, d=1. So duplicates are l, o.
        "aabbccd",          # Expected duplicate: a, b, c
        "abcdef",           # No duplicates expected -> []
        "python programming", 
    ]

    for test_input in test_cases:
        result = analyzer.check_for_duplicates(test_input)
        print(f"Input: '{test_input}'")
        if not result:
            print("No duplicate characters found.")
        else:
            # Join the list of single-character strings to display cleanly
            unique_dupes_str = " ".join(result).upper() + " (Count > 1)"
            dup_count_text = ", count > 1".lower() if len(unique_dupes_str) == 0 else ""