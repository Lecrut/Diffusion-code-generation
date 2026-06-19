class FirstLetterExtractor:
    def __init__(self):
        self.punctuation_map = {'.': '', ',': '', '?': '', '!': ''}

    def extract(self, text):
        words = text.split()
        first_letters = []
        for word in words:
            cleaned_word = ''.join(self.punctuation_map.get(char, char) for char in word)
            if cleaned_word:
                first_letters.append(cleaned_word[0])
        return first_letters

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Hello, world! This is a test."
    result = extractor.extract(sample_text)
    print(result)