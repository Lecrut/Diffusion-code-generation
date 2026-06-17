class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair_key, combined_value):
        if isinstance(word_pair_key, tuple) and len(word_pair_key) == 2:
            key_str = f"{word_pair_key[0]}-{word_pair_key[1]}"
            self._data[key_str] = combined_value
        else:
            raise ValueError("Key must be a pair of words")
    def get(self, word_pair_key):
        if isinstance(word_pair_key, tuple) and len(word_pair_key) == 2:
            key_str = f"{word_pair_key[0]}-{word_pair_key[1]}"
            return self._data.get(key_str)
        else:
            raise ValueError("Key must be a pair of words")
    def remove(self, word_pair_key):
        if isinstance(word_pair_key, tuple) and len(word_pair_key) == 2:
            key_str = f"{word_pair_key[0]}-{word_pair_key[1]}"
            return self._data.pop(key_str, None)
        else:
            raise ValueError("Key must be a pair of words")
    def __contains__(self, word_pair_key):
        if isinstance(word_pair_key, tuple) and len(word_pair_key) == 2:
            key_str = f"{word_pair_key[0]}-{word_pair_key[1]}"
            return key_str in self._data
        else:
            raise ValueError("Key must be a pair of words")
    def __len__(self):
        return len(self._data)
    def items(self):
        result = []
        for k, v in self._data.items():
            word_pair_key = tuple(k.split("-"))
            if isinstance(word_pair_key, tuple) and len(word_pair_key) == 2:
                result.append((word_pair_key, v))
        return result
    def __str__(self):
        items_str = ", ".join(f"{k}={v}" for k, v in self.items())
        return f"{{ {items_str} }}"
if __name__ == '__main__':
    d = WordPairDict()
    d.add(("hello", "world"), "helloworld")
    d.add(("python", "code"), "pythoneode")
    assert ("hello", "world") in d
    assert len(d) == 2
    retrieved = d.get(("hello", "world"))
    assert retrieved == "helloworld"
    removed = d.remove(("python", "code"))
    assert removed == "pythoneode"
    print("All assertions passed successfully.")