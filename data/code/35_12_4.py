class VowelCounter:
    """A class to count vowels in a given string."""

    def __init__(self):
        self._vowels = set("aeiouAEIOU")

    def count(self, text: str) -> int:
        """Calculate and return the number of vowels in the input string.

        Args:
            text (str): The string to search for vowels.

        Returns:
            int: The total count of vowel characters found.
        """
        return sum(1 for char in text if char in self._vowels)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or network access is needed
    samples = [
        "Hello, World!",
        "AEIOUaeiou",
        "",
        "Python Programming",
        "The quick brown fox jumps over the lazy dog"
    ]

    counter = VowelCounter()

    for sample in samples:
        result = counter.count(sample)
        print(f"'{sample}' has {result} vowels.")