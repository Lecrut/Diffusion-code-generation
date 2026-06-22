import re

class StringProcessor:
    @staticmethod
    def remove_spaces(sentence):
        return re.sub(r'\s+', '', sentence)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_sentence = "This is a sample sentence with extra spaces"
    print(processor.remove_spaces(sample_sentence))