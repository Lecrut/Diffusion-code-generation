class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add_pair(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if not isinstance(key, tuple):
            raise TypeError("Key must be a pair of strings")
        self._data[key] = value
    def get_pair(self, word1: str, word2: str) -> str | None:
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def __contains__(self, pair):
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise TypeError("Pair must be a tuple of two strings")
        return pair[0].lower() in [k[0] for k in self._data.keys()] and \
               any(k == (pair[0].lower(), pair[1].lower()) or k == (pair[1].lower(), pair[0].lower()) for k in self._data.keys())
    def __iter__(self):
        return iter(self._data.items())
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add_pair("Hello", "World")
    d.add_pair("HELLO", "WORLD")
    print(d.get_pair("hello", "world"))               
    if d.get_pair("hello", "world") is not None:
        exit_code = 0
    else:
        exit_code = 1
    exit(exit_code)