class FirstLetterExtractor:
    def extract(self, text):
        if not text:
            return []
        words = text.split()
        return [word[0] for word in words if word]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    result = extractor.extract("Hello World Python")
    print(result)