class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in self.input_string:
            if char in vowels:
                count += 1
        return count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    processor = StringProcessor(sample_string)
    print(processor.count_vowels())