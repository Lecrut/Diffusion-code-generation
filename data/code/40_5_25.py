import string

class WordProcessor:
    def __init__(self, text):
        self.text = text

    def get_first_letters(self):
        result = {}
        words = self.text.split()
        for word in words:
            cleaned_word = ''.join(char for char in word if char.isalpha())
            if cleaned_word:
                result[cleaned_word] = cleaned_word[0]
        return result

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test."
    sample_string2 = "Python is fun, isn't it?"
    sample_string3 = "  What's up?  End."

    processor1 = WordProcessor(sample_string1)
    print(processor1.get_first_letters())

    processor2 = WordProcessor(sample_string2)
    print(processor2.get_first_letters())

    processor3 = WordProcessor(sample_string3)
    print(processor3.get_first_letters())