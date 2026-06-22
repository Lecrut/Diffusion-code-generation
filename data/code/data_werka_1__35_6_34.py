class StringProcessor:
    def count_vowels(self, input_string):
        vowels = set('aeiouAEIOU')
        count = 0
        for char in input_string:
            if char in vowels:
                count += 1
        return count

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello, World!"
    print(processor.count_vowels(sample_string))