class SentenceCapitalizer:
    def __init__(self, sentence):
        self.sentence = sentence

    def capitalize_first_letter(self):
        return ' '.join(word.capitalize() for word in self.sentence.split())

if __name__ == '__main__':
    sample_sentence1 = "hello world, this is an example sentence."
    capitalizer1 = SentenceCapitalizer(sample_sentence1)
    capitalized_sentence1 = capitalizer1.capitalize_first_letter()
    print(capitalized_sentence1)

    sample_sentence2 = "another test sentence with multiple words."
    capitalizer2 = SentenceCapitalizer(sample_sentence2)
    capitalized_sentence2 = capitalizer2.capitalize_first_letter()
    print(capitalized_sentence2)