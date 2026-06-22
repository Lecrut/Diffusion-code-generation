class SentenceCapitalizer:
    def __init__(self, sentence):
        self.sentence = sentence

    def capitalize_first_letter(self):
        return ' '.join(word.capitalize() for word in self.sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    capitalizer = SentenceCapitalizer(sample_sentence)
    capitalized_sentence = capitalizer.capitalize_first_letter()
    print(capitalized_sentence)