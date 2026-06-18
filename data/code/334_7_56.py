class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower())
        combined = f"{key[0]}-{key[1]}"
        if not isinstance(key, tuple):
            raise TypeError("Key must be a pair of strings")
    def get(self, word1: str, word2: str) -> str | None:
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def __contains__(self, item):
        if isinstance(item, tuple) and len(item) == 2:
            return item in self._data
        return False
    def update(self, pairs_data: dict[tuple[str, str], str]) -> None:
        for key, value in pairs_data.items():
            if not (isinstance(key, tuple) and isinstance(key[0], str)):
                raise ValueError("All keys must be tuples of strings")
            self._data[key] = value
    def __repr__(self):
        return f"WordPairDictionary({dict(self._data)})"
if __name__ == '__main__':
    d = WordPairDictionary()
    pairs_data = {('hello', 'world'): "HELLO-WORLD", ('foo', 'bar'): "FOO-BAR"}
    d.update(pairs_data)
    result1 = d.get("Hello", "World")
    if not isinstance(result1, str):
        raise RuntimeError(f"Expected string, got {type(result1)}")
    print(result1)