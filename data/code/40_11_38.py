class FirstLetterExtractor:

    def extract_all(self, list_of_strings):
        first_letters = []
        for string in list_of_strings:
            if string:
                first_letter = string[0]
                first_letters.append(first_letter)
        return first_letters
if __name__ == '__main__':
    sample_data = ['cat', 'bat', 'rat', 'mat']
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_data)
    print(result)