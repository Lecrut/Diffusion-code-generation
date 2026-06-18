class VowelCounter:
    def __init__(self):
        self._vowels = set("aeiouAEIOU")
    
    def count(self, text) -> int:
        """Returns the number of vowels in the input string."""
        if not isinstance(text, str):
            raise TypeError(f"Expected string input, got {type(text).__name__}")
        return sum(1 for char in text if char in self._vowels)

if __name__ == '__main__':
    counter = VowelCounter()

    test_cases = [
        "Hello World",  # Expected: H-e-llo W-orld -> e, o, o (3? or 2 depending on interpretation of 'y') - treating y as vowel here: 4)
        "Python Programming",
        "",             # Empty string
        "aeiou AEIOU ", # Uppercase and lowercase mix with space
    ]

    for test_input in test_cases:
        count_result = counter.count(test_input)
        print(f"Text: '{test_input}'")
        print(f"Vowel Count: {count_result}")
        
        # Additional debug to verify correctness on the first sample where y is typically NOT counted as a vowel strictly, 
        # but often in simple tasks it might be. Here we stick to standard definition excluding 'y'.
        # "Hello World": e, o, o -> 3 vowels (excluding y).
        if test_input == "Hello World":
            assert count_result == 3, f"Expected 3 for 'Hello World', got {count_result}"