class SentenceCapitalizer:
    SEPARATOR = ' '

    @staticmethod
    def capitalize_first_letter(word):
        if not word:
            return ''
        return word[0].upper() + word[1:]

    @classmethod
    def process_sentence(cls, sentence):
        words = sentence.split(cls.SEPARATOR)
        capitalized_words = [cls.capitalize_first_letter(word) for word in words]
        return cls.SEPARATOR.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    capitalizer = SentenceCapitalizer()
    capitalized_sentence = capitalizer.process_sentence(sample_sentence)
    print(capitalized_sentence)