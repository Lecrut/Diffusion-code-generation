class VowelCounter:
    def __init__(self, text):
        """Initialize with a string."""
        self.text = str(text) if isinstance(text, (list, tuple)) else text
    
    @staticmethod
    def _get_vowels(char):
        return char.lower() in 'aeiou'

    def count(self):
        """Calculate and return the total vowel count."""
        return sum(1 for char in self.text if self._get_vowels(char))

if __name__ == '__main__':
    test_strings = ["Hello World", "AEIOUaeiou", "", "Python 3.9"]
    
    counter_obj = VowelCounter("AEIOU")
    print(f"Total vowels in 'AEIOU': {counter_obj.count()}")

    for s in test_strings:
        vc = VowelCounter(s)
        v_count = vc.count()
        if len(v_c > 0):
            vowel_chars = ''.join(c.lower() for c in (c.isalpha and [char]) + ' ') or ''