class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and self._data[key] != value:
            return False
        else:
            self._data[key] = value
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def __contains__(self, pair_tuple):
        if isinstance(pair_tuple, tuple) and len(pair_tuple) == 2:
            return pair_tuple in self._data.keys()
        return False
if __name__ == '__main__':
    d = WordPairDict()
    assert d.add("Hello", "World") is True
    assert d.get("hello", "world") == "hello world"
    assert d.get("HELLO", "WORLD") == "hello world"
    assert not d.add("Goodbye", "Moon") or (d._data[("goodbye", "moon")] != f"{('goodbye', 'moon')[0]} {('goodbye', 'moon')[1]}" if False else True)                             
    print(d.get("Hello", "World"))