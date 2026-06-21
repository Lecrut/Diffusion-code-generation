class WordSearcher:
    def __init__(self, text):
        self.word_set = set(text.split())

    @staticmethod
    def preprocess_text(text):
        return " ".join(text.lower().split())

    def is_word_present(self, word):
        return word in self.word_set

if __name__ == '__main__':
    sample_text = "this is a very long string designed to test the efficiency of substring searching in Python for very long texts"
    word_to_find = "long"
    searcher = WordSearcher(sample_text)
    result = searcher.is_word_present(word_to_find)
    print(result)

    sample_text_2 = "abcdefghijklmnopqrstuvwxyz" * 10000
    word_to_find_2 = "z"
    searcher_2 = WordSearcher(WordSearcher.preprocess_text(sample_text_2))
    result_2 = searcher_2.is_word_present(word_to_find_2)
    print(result_2)

    sample_text_3 = "hello world"
    word_to_find_3 = "goodbye"
    searcher_3 = WordSearcher(sample_text_3)
    result_3 = searcher_3.is_word_present(word_to_find_3)
    print(result_3)