import re

class StringSeparator:
    def separate_characters(self, input_string):
        return re.findall(r'\b.\b', input_string)

if __name__ == '__main__':
    separator = StringSeparator()
    sample_string = "Hello123World!"
    separated_chars = separator.separate_characters(sample_string)
    print(separated_chars)