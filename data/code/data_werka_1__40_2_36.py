class FirstLetterExtractor:
    def extract(self, text):
        words = text.split()
        first_letters = [word[0] for word in words if word]
        return ''.join(first_letters)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Hello World from Alibaba Cloud"
    result = extractor.extract(sample_text)
    print(result)