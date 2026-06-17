class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        pair_key = (word1, word2)
        combined_value = f"{word1}-{word2}"
        if not isinstance(pair_key, tuple) or len(pair_key) != 2:
            raise ValueError("Key must be a pair of two strings.")
        self._data[pair_key] = combined_value
    def get(self, word1: str, word2: str):
        key = (word1, word2)
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    result = d.get("apple", "banana")
    assert result == "apple-banana"
    exit(0)