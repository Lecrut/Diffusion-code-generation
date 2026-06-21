import re

class StringSeparator:
    DELIMITERS = r'[^a-zA-Z0-9]'

    @staticmethod
    def separate_characters(input_string):
        return re.findall(r'\w', input_string)

if __name__ == '__main__':
    sample_string = "Hello123World!"
    result = StringSeparator.separate_characters(sample_string)
    print(result)