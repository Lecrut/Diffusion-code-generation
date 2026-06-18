class VowelCounter:
    """A class to count vowels in a given string."""
    
    def __init__(self):
        # Define set of lowercase vowels for efficient lookup
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def count(self, text: str) -> int:
        """
        Count the number of vowels in the input string.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            int: The total count of vowels found in the string.
        """
        # Convert text to lowercase for case-insensitive comparison and use set intersection logic implicitly via generator expression
        return sum(1 for char in text.lower() if char in self.vowels)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    test_cases = [
        "Hello, World!",           # Expected: 3 ('e', 'o', 'o')
        "AEIOU",                   # Expected: 5
        "",                        # Expected: 0
        "Python Programming 2.0"   # Expected: 4 ('y' is not counted here based on standard definition, so a,e,o,i -> e,o,i? Wait: P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g... vowels are o, o, a, i = 4)
    ]

    counter = VowelCounter()

    for text in test_cases:
        result = counter.count(text)
        print(f"Text: '{text}' -> Count: {result}")