class FirstLetterExtractor:
    def extract(self, text):
        words = self._split_text(text)
        first_letters = [self._get_first_letter(word) for word in words if word]
        return ''.join(first_letters)

    def _split_text(self, text):
        return text.split()

    def _get_first_letter(self, word):
        return word[0]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Extract the first letter of each word"
    result = extractor.extract(sample_text)
    print(result)