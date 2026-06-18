class Dictionary:
    def __init__(self):
        self._data = {}
    def add(self, key_pair, value_string):
        if isinstance(key_pair, tuple) and len(key_pair) == 2:
            word1, word2 = key_pair
            combined = f"{word1}{word2}"
            self._data[key_pair] = combined
            return True
        else:
            raise ValueError("Key must be a pair of two words")
    def get(self, key_pair):
        if isinstance(key_pair, tuple) and len(key_pair) == 2:
            word1, word2 = key_pair
            combined = f"{word1}{word2}"
            return self._data.get(key_pair, None)
        else:
            raise ValueError("Key must be a pair of two words")
    def optimize_lookup(self):
        optimized_map = {}
        for k in self._data.keys():
            if isinstance(k, tuple) and len(k) == 2:
                word1, word2 = k
                combined_key = f"{word1}{word2}"
                optimized_map[combined_key] = self._data[k]
        return optimized_map
if __name__ == '__main__':
    d = Dictionary()
    d.add(('hello', 'world'), "helloworld")
    d.add(('python', 'code'), "pythongode")
    result_optimized = d.optimize_lookup()
    print(result_optimized)