class StringProcessor:
    def count_vowels(self, text):
        count = 0
        vowels = "aeiouAEIOU"
        for char in text:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello World"
    result = processor.count_vowels(sample_string)
    print(result)