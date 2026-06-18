class StringProcessor:
    def get_first_letters(self, text):
        words = [word for word in text.split() if word]
        return ''.join(word[0].lower() for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World This Is A Test"
    result = processor.get_first_letters(sample_input)
    print(result)