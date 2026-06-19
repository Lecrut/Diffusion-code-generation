class StringProcessor:
    def count_vowels(self, s):
        vowels = set('aeiouAEIOU')
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello, World!"
    print(processor.count_vowels(sample_string))