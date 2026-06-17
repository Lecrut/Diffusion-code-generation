class Dictionary:
    def __init__(self):
        self._data = {}
    def add(self, key_pair, value_str):
        if isinstance(key_pair, tuple) and len(key_pair) == 2:
            word1, word2 = key_pair
            combined_value = f"{word1}{value_str}"
            self._data[key_pair] = combined_value
        else:
            raise ValueError("Key must be a pair of strings")
    def get(self, key_pair):
        if isinstance(key_pair, tuple) and len(key_pair) == 2:
            return self._data.get(key_pair)
        return None
if __name__ == '__main__':
    d = Dictionary()
    d.add(("apple", "pie"), "")
    result = d.get(("apple", "pie"))
    assert result is not None and len(result) > 0, "Test failed"
    print("Success")