class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            key = (word_pair[0], word_pair[1])
            value = f"{word_pair[0]}{word_pair[1]}"
            self._data[key] = value
    def get(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            return self._data.get((word_pair[0], word_pair[1]))
        return None
if __name__ == '__main__':
    d = WordPairDict()
    d.add(("hello", "world"))
    d.add(("foo", "bar"))
    print(d.get(("hello", "world")))               
    assert d.get(("hello", "world")) == "helloworld"
    exit(0)