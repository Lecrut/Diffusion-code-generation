class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add_pair(self, word1: str, word2: str) -> None:
        combined_key = (word1, word2)
        if combined_key not in self._data:
            value = f"{word1}-{word2}"
            self._data[combined_key] = value
    def get_combined(self, word1: str, word2: str) -> str | None:
        key = (word1, word2)
        return self._data.get(key)
    def __repr__(self):
        items = [f"{k}={v}" for k, v in sorted(self._data.items())]
        return f"WordPairDictionary({', '.join(items)})"
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add_pair("apple", "banana")
    d.add_pair("cat", "dog")
    result1 = d.get_combined("apple", "banana")
    result2 = d.get_combined("zebra", "monkey")
    print(result1)                
    print(result2)