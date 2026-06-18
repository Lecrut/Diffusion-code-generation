class VowelCounter:
    def __init__(self, text):
        self.text = str(text) if isinstance(text, (bytes, bytearray)) else str(text)

    def count_vowels(self):
        """Calculate and return the total number of vowels in the string."""
        lowercase_text = self.text.lower()
        vowel_set = set('aeiou')
        return sum(1 for char in lowercase_text if char in vowel_set)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input, stdin, or args)
    test_strings = [
        "Hello World!",
        "AEIOU",
        "",
        "Python Programming"
    ]

    for s in test_strings:
        counter = VowelCounter(s)
        count = counter.count_vowels()
        print(f"'{s}' has {count} vowels.")