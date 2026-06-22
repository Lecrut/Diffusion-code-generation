class StringProcessor:
    def count_vowels(self, s):
        vowels = set('aeiouAEIOU')
        return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello, World!"
    print(processor.count_vowels(sample_string))