class FirstLetterExtractor:
    def extract_all(self, string_list):
        first_letters = []
        for s in string_list:
            if s:
                first_letters.append(s[0])
        return first_letters
if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["Apple", "Banana", "Cherry", "Date", ""]
    result = extractor.extract_all(sample_strings)
    print(result)