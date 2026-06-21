class TextSearcher:
    def __init__(self, text):
        self.word_set = set(text.split())

    def contains_word(self, word):
        return word in self.word_set

if __name__ == '__main__':
    large_text = "this is a very long string designed to test the efficiency of substring searching in Python for very long texts. we need to ensure that this search operation is as fast as possible even when the text body is massive and the word might be located anywhere within it."
    word1 = "long"
    word2 = "massive"
    word3 = "nonexistent"
    searcher = TextSearcher(large_text)
    result1 = searcher.contains_word(word1)
    result2 = searcher.contains_word(word2)
    result3 = searcher.contains_word(word3)
    print(f"Does the text contain '{word1}'? {result1}")
    print(f"Does the text contain '{word2}'? {result2}")
    print(f"Does the text contain '{word3}'? {result3}")