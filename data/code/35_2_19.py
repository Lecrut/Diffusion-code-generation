class VowelCounter:
    def __init__(self, text):
        """
        Initialize the VowelCounter with a given string.
        
        Args:
            text (str): The input string to analyze for vowels.
        """
        self.text = str(text) if isinstance(text, str) else ""

    def count_vowels(self):
        """
        Calculate and return the total count of vowels in the stored string.
        
        Returns:
            int: Total number of vowels (both uppercase and lowercase).
        """
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.text if char in vowels)

if __name__ == "__main__":
    # Hard-coded sample values to ensure no user input, networking, or files are required.
    test_strings = [
        "Hello World",
        "AEIOU aeiou AEIOU",
        "",
        "Rhythm and Blues"
    ]

    for test_str in test_strings:
        counter = VowelCounter(test_str)
        count = counter.count_vowels()
        print(f"'{test_str}' -> {count} vowels")