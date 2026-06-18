class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word_pair_str):
        words = list(word_pair_str.split())
        if len(words) != 2:
            raise ValueError("Input must contain exactly two words.")
        key = tuple(words[:])                                             
        self._data[key] = " ".join(words)
    def get(self, word_pair_tuple):
        return self._data.get(word_pair_tuple, None)
    def __contains__(self, item):
        if isinstance(item, str):
            words = list(item.split())
            key = tuple(words[:])
            return len(key) == 2 and key in self._data
        elif isinstance(item, tuple):
            return item[0] is not None and item[1] is not None and item in self._data
        else:
            raise TypeError("Item must be a string or tuple of two words.")
    def __repr__(self):
        items = [f"({k}, {v})" for k, v in sorted(self._data.items())]
        return f"{type(self).__name__}({', '.join(items)})"
if __name__ == '__main__':
    d = WordPairDictionary()
    samples = [
        "hello world",
        "python programming",
        "code logic",
        "data science"
    ]
    for s in samples:
        d.add(s)
    print(d)
    test_queries = ["hello world", ("python", "programming"), "wrong pair"]
    result1 = d.get(("hello", "world"))
    result2 = d.get(("nonexistent", "word"))
    exists_hello_world = "hello world" in d
    assert result1 == "hello world", f"Expected 'hello world', got {result1}"
    assert result2 is None, f"Expected None for missing key, got {result2}"
    print("All tests passed.")