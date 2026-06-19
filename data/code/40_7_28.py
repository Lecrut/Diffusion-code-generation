import re

class StringProcessor:

    def find_first_letters(self, text: str) -> list:
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        words = re.findall('\\b\\w+\\b', text)
        first_letters = [word[0] for word in words if word.isalpha()]
        return first_letters
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = 'Hello world, this is a test.'
    sample_string_2 = '   \t\nStart here.'
    sample_string_3 = '123numbers'
    sample_string_4 = '!@#$%^&*()'
    print(processor.find_first_letters(sample_string_1))
    print(processor.find_first_letters(sample_string_2))
    print(processor.find_first_letters(sample_string_3))
    print(processor.find_first_letters(sample_string_4))