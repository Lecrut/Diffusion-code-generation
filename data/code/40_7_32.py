class StringProcessor:

    def __init__(self):
        self.punctuation = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    def is_word_start(self, char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    def find_first_word_initials(self, text: str) -> list:
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        initials = []
        in_word = False
        for char in text:
            if self.is_word_start(char):
                if not in_word:
                    initials.append(char)
                    in_word = True
            elif char in self.punctuation or char.isspace():
                in_word = False
        return initials
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = 'Hello world, this is a test.'
    sample_string_2 = '   \t\nStart here.'
    sample_string_3 = '123numbers'
    sample_string_4 = '!@#$%^&*()'
    sample_string_5 = 'A quick brown fox jumps over the lazy dog.'
    print(processor.find_first_word_initials(sample_string_1))
    print(processor.find_first_word_initials(sample_string_2))
    print(processor.find_first_word_initials(sample_string_3))
    print(processor.find_first_word_initials(sample_string_4))
    print(processor.find_first_word_initials(sample_string_5))