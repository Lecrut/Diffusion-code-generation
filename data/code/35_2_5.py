class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text) if isinstance(text, (list, tuple)) else str(text)

    def count_vowels(self):
        """Calculate and return the total vowel count in lowercase only.
        
        Vowels are defined as 'a', 'e', 'i', 'o', 'u'.
        """
        vowels = set("aeiou")
        return sum(1 for char in self.text if char.lower() in vowels)

if __name__ == '__main__':
    # Hard-coded sample values; no user input or network access.
    samples = [
        "hello world",          # 2 vowels (e, o)
        "Python is awesome!",  # 4 vowels (y/i/o/a/e - note: y usually not counted here unless specified otherwise based on strict aeiou set; using standard 'aeiou' logic -> i,o,a,e = 4 if case-insensitive and excluding y. Wait: P-y-t-h-o-n-i-s-a-w-e-s-! -> o, i, a, e = 4)
        "AEIOU",               # 5 vowels (uppercase handled by .lower())
        "",                    # 0 vowels
        "aeiouybcdfg"          # 5 vowels ('a', 'e', 'i', 'o', 'u' - y is excluded in this strict definition)
    ]

    for sample_text in samples:
        counter = VowelCounter(sample_text)
        count = counter.count_vowels()
        print(f"Text: '{sample_text}' -> Count: {count}")