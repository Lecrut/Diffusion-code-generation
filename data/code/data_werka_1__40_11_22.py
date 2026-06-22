class FirstLetterExtractor:
    def extract_all(self, list_of_strings):
        first_letters = []
        for string in list_of_strings:
            if string:
                first_letters.append(string[0])
        return first_letters

if __name__ == '__main__':
    sample_data = ["dog", "elephant", "frog", "giraffe"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_data)
    print(result)