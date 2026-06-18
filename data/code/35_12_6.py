class VowelCounter:
    """A class to count vowels in a given text string."""

    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def count(self, text: str) -> int:
        """
        Efficiently calculates and returns the number of vowels in the input string.

        Args:
            text (str): The input string to analyze.

        Returns:
            int: The total count of vowel characters in the text.
        """
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    
    # Hard-coded sample values without user input or external dependencies
    test_cases = [
        ("Hello, World!", 2),      # o, o
        ("AEIOU", 5),               # All uppercase vowels
        ("aeiou", 5),               # All lowercase vowels
        ("Python Programming", 3),  # y is not counted here based on standard definition (a,e,i,o,u) -> a, i, o? Wait: P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g. Vowels: o, o, a, i. That's 4. Let's correct sample logic in comment below or adjust string.)
        # Correction for Python Programming: 
        # 'o' (index 5), 'o' (index 9), 'a' (index 13), 'i' (index 16). Count = 4.
        ("Python Programming", 4), 
    
    ]

    for test_input, expected_count in test_cases:
        result = counter.count(test_input)
        print(f"Input: '{test_input}' -> Vowel count: {result}")
        
# Ensure the module runs without errors on its own execution.