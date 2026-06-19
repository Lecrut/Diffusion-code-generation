class VowelCounter:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")
        self.text = text

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    sample_string = "Example String with Vowels"
    try:
        counter = VowelCounter(sample_string)
        vowel_count = counter.count_vowels()
        print(vowel_count)
    except ValueError as e:
        print(e)