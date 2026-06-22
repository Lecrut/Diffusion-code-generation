class FirstLetterExtractor:

    def __init__(self, text):
        self.text = text

    def extract_first_letters(self):
        words = self.text.split()
        first_letters = [word[0] for word in words if word]
        return first_letters
if __name__ == '__main__':
    sample_text1 = 'Hello world'
    sample_text2 = '   \t '
    sample_text3 = 'Single'
    sample_text4 = 'One   two   three'
    extractor1 = FirstLetterExtractor(sample_text1)
    print(extractor1.extract_first_letters())
    extractor2 = FirstLetterExtractor(sample_text2)
    print(extractor2.extract_first_letters())
    extractor3 = FirstLetterExtractor(sample_text3)
    print(extractor3.extract_first_letters())
    extractor4 = FirstLetterExtractor(sample_text4)
    print(extractor4.extract_first_letters())