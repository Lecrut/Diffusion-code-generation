class SentenceSearcher:
    def __init__(self):
        self.word_set = set()

    @staticmethod
    def split_sentence_into_words(sentence: str) -> set:
        return set(sentence.split())

    def add_sentences_to_word_set(self, sentences: list):
        for sentence in sentences:
            self.word_set.update(self.split_sentence_into_words(sentence))

    def check_term_presence(self, term: str) -> bool:
        return term in self.word_set

if __name__ == '__main__':
    searcher = SentenceSearcher()
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a versatile and powerful programming language",
        "Data structures are essential for efficient algorithms"
    ]
    searcher.add_sentences_to_word_set(sample_sentences)
    target_term = "powerful"
    print(f"Target Term: {target_term}")
    print(f"Term Present: {searcher.check_term_presence(target_term)}")