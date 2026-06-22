class SentenceCapitalizer:
    def __init__(self, sentence):
        self.sentence = sentence

    @staticmethod
    def capitalize_word(word):
        return word.capitalize()

    def capitalize_sentence(self):
        words = self.sentence.split()
        capitalized_words = [self.capitalize_word(word) for word in words]
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    capitalizer = SentenceCapitalizer(sample_sentence)
    capitalized_sentence = capitalizer.capitalize_sentence()
    print(capitalized_sentence)