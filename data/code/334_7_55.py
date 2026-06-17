class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1, word2)
        if key in self._data:
            combined = self._data[key] + f" {key[0]}{key[1]}"
        else:
            combined = f"{word1}{word2}"
        self._data[key] = combined
    def get(self, word1: str, word2: str) -> str:
        key = (word1, word2)
        return self._data.get(key, "")
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("apple", "banana")
    d.add("cherry", "date")
    print(d.get("apple", "banana"))