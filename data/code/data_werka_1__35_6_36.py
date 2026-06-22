class StringProcessor:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels = set('aeiouAEIOU')
        count = 0
        for char in self.text:
            if char in vowels:
                count += 1
        return count

if __name__ == '__main__':
    sample_text = "Hello, World!"
    processor = StringProcessor(sample_text)
    print(processor.count_vowels())