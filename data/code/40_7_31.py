import re

class StringProcessor:

    def find_first_word_initials(self, text: str) -> list:
        words = re.findall('\\b\\w+\\b', text)
        initials = [word[0] for word in words if word.isalpha()]
        return initials
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = 'Hello world, this is a test.'
    sample_string_2 = '   \t\nStart here!'
    sample_string_3 = '123numbers'
    sample_string_4 = 'Punctuation!!! Only!!!'
    sample_string_5 = ''
    print(processor.find_first_word_initials(sample_string_1))
    print(processor.find_first_word_initials(sample_string_2))
    print(processor.find_first_word_initials(sample_string_3))
    print(processor.find_first_word_initials(sample_string_4))
    print(processor.find_first_word_initials(sample_string_5))