class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and self._data[key] != value:
            raise ValueError(f"Duplicate entry with different values for keys {key}")
        self._data[key] = value
    def get(self, word1: str, word2: str) -> str | None:
        return self._data.get((word1.lower(), word2.lower()))
    def __repr__(self):
        return f"WordPairDict({list(self._data.items())})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    d.add("Apple", "Banana")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    pass
d = WordPairDict()
try:
    d.add("apple", "banana")
except ValueError:
    pass                                                                                                                                                                                                                
d.add("apple", "banana")
print(d.get("Apple", "Banana"))                                                                                                                                                                                                    
class WordPairDictOptimized:
    def __init__(self):
        self._data = {}
    def _normalize_key(self, word1: str, word2: str) -> tuple[str, str]:
        return (word1.lower(), word2.lower())
    def add(self, word1: str, word2: str) -> None:
        key = self._normalize_key(word1, word2)
        value = f"{key[0]} {key[1]}"
        self._data[key] = value
    def get(self, word1: str, word2: str) -> str | None:
        key = self._normalize_key(word1, word2)
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDictOptimized()
    d.add("apple", "banana")
    print(d.get("Apple", "Banana"))                                 
class WordPairDictOptimized:
    def __init__(self):
        self._data = {}
    def _normalize_key(self, word1: str, word2: str) -> tuple[str, str]:
        return (word1.lower(), word2.lower())
    def add(self, word1: str, word2: str) -> None:
        key = self._normalize_key(word1, word2)
        value = f"{key[0]} {key[1]}"
        self._data[key] = value
    def get(self, word1: str, word2: str) -> str | None:
        key = self._normalize_key(word1, word2)
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDictOptimized()
    d.add("apple", "banana")
    print(d.get("Apple", "Banana"))