import re

class StringProcessor:

    def extract_initials(self, text: str) -> list:
        WORD_PATTERN = '\\b[a-zA-Z]'
        matches = re.findall(WORD_PATTERN, text)
        return matches
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = 'Hello world! This is a test.'
    sample_string_2 = '   \t\nStart here with punctuation!!!'
    sample_string_3 = '123numbers and symbols #$%'
    sample_string_4 = ''
    sample_string_5 = '   '
    print(processor.extract_initials(sample_string_1))
    print(processor.extract_initials(sample_string_2))
    print(processor.extract_initials(sample_string_3))
    print(processor.extract_initials(sample_string_4))
    print(processor.extract_initials(sample_string_5))