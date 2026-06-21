import string

class WordInitialExtractor:
    PUNCTUATION = set(string.punctuation)

    @staticmethod
    def is_alpha(word):
        return any(char.isalpha() for char in word)

    def extract_initials(self, input_string):
        words = input_string.split()
        initials = []
        for word in words:
            stripped_word = ''.join(char for char in word if char not in self.PUNCTUATION)
            if self.is_alpha(stripped_word):
                initials.append(stripped_word[0])
        return initials

if __name__ == '__main__':
    extractor = WordInitialExtractor()
    sample_input_1 = 'Hello, world! This is a test... with some punctuation!!!'
    sample_input_2 = '   Leading spaces and punctuation!!!'
    sample_input_3 = '123numbers only'
    sample_input_4 = '!@#$%^&*() no words here'
    
    print(extractor.extract_initials(sample_input_1))
    print(extractor.extract_initials(sample_input_2))
    print(extractor.extract_initials(sample_input_3))
    print(extractor.extract_initials(sample_input_4))