class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            key = ('a', 'b') if all(isinstance(x, str) for x in word_pair) else None
            combined_str = ''.join(word_pair).lower()
            self._data[key] = combined_str
    def get(self):
        return dict(sorted(self._data.items()))
if __name__ == '__main__':
    d = WordPairDict()
    sample_pairs = [('Hello', 'World'), ('Python', 'Code')]
    for pair in sample_pairs:
        d.add(pair)
    result = d.get()
    print(result)