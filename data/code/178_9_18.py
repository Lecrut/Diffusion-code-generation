import numpy as np

class StringProcessor:
    @staticmethod
    def extract_unique_words(strings):
        words = np.char.split(np.array(strings), sep=' ')
        flat_words = [word for sublist in words for word in sublist]
        unique_words = list(set(flat_words))
        return unique_words

if __name__ == '__main__':
    processor = StringProcessor()
    sample_strings = ["Hello World this is a Test String", "This Is A Sample String With Mixed Cases"]
    unique_word_list = processor.extract_unique_words(sample_strings)
    print("Unique Words:", unique_word_list)