class StringProcessor:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels = set('aeiouAEIOU')
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    sample_text = "Hello World"
    processor = StringProcessor(sample_text)
    print(processor.count_vowels())