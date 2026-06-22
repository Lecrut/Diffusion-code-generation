class FirstLetterExtractor:
    def extract(self, text):
        words = text.split()
        return ''.join(word[0] for word in words if word)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Unique implementation of the task"
    result = extractor.extract(sample_text)
    print(result)