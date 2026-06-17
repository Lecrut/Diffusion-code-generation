class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        if word1 not in self._data:
            self._data[word1] = []
        self._data[word1].append(word2)
    def get_combined_string(self, key_word_pair):
        words = [key_word_pair[0], key_word_pair[1]]
        return " ".join(words)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("python", "code")
    result_key = ("hello", "world")
    combined_str = d.get_combined_string(result_key)
    assert combined_str == "hello world"