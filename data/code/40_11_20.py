class FirstLetterExtractor:
    def extract_all(self, strings):
        result = []
        for string in strings:
            if string:
                result.append(string[0])
        return result

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["hello", "world", "python", "code"]
    first_letters = extractor.extract_all(sample_strings)
    print(first_letters)