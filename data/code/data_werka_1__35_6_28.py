class StringProcessor:
    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count

if __name__ == '__main__':
    processor = StringProcessor()
    sample_text = "Hello, World!"
    print(processor.count_vowels(sample_text))