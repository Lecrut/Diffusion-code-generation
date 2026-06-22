class UppercaseExtractor:
    def extract_uppercase(self, input_string):
        return ''.join(char for char in input_string if char.isupper())

if __name__ == '__main__':
    extractor = UppercaseExtractor()
    sample_string = "This is a complex string with numbers 123 and symbols!@#$ %^&*()"
    result = extractor.extract_uppercase(sample_string)
    print(result)