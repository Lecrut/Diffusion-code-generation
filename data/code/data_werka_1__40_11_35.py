class FirstLetterExtractor:
    def extract_all(self, list_of_strings):
        if not list_of_strings:
            return []
        
        first_letters = [s[0] for s in list_of_strings if s]
        return first_letters

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_list)
    print(result)