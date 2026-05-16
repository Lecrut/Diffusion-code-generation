class FirstLetterExtractor:
    def extract_all(self, list_of_strings):
        first_letters = []
        for s in list_of_strings:
            if s:
                first_letters.append(s[0])
        return first_letters
if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["apple", "banana", "cherry", "date", ""]
    result = extractor.extract_all(sample_strings)
    print(result)