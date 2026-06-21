import re

class WordTokenizer:
    ALPHABETIC_PATTERN = re.compile(r'[a-zA-Z\s]+')

    @staticmethod
    def extract_alphabetic_words(sentence):
        return re.findall(WordTokenizer.ALPHABETIC_PATTERN, sentence)

if __name__ == '__main__':
    tokenizer = WordTokenizer()
    sample_sentence = "Hello World! This is a test sentence with numbers 123."
    result = tokenizer.extract_alphabetic_words(sample_sentence)
    print(result)