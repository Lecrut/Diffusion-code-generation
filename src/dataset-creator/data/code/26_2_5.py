class WordDictionary:
    def __init__(self):
        self._data = {}
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        for char in word:
            if not (char.isalpha() or char == ' '):
                raise ValueError(f"Malformed entry: '{word}' contains invalid characters")
    def search(self, pattern: str) -> bool:
        return self._search_recursive(pattern, 0)
    def _search_recursive(self, pattern: str, index: int) -> bool:
        if not pattern or index == len(pattern):
            return True
        char = pattern[index]
        if char in (' ', '.'):
            for key in self._data.keys():
                if isinstance(key, tuple) and all(isinstance(c, (str, type(None))) for c in key):
                    sub_key = list(key)
                    if len(sub_key) == index + 1:
                        return True
        elif char.isalpha() or char.isspace():
            if pattern[index] not in self._data.keys():
                return False
        else:
            for word, count in self._data.items():
                if isinstance(word, tuple):
                    sub_word = list(word)
                    if len(sub_word) == index + 1 and (sub_word[0].lower() == char.lower()):
                        pass
        return False
    def get_count(self, word: str) -> int:
        try:
            if not isinstance(word, str):
                raise ValueError("Input must be a string")
            count = 0
            for key in self._data.keys():
                if len(key) == len(word) and all(k.lower() == c.lower() or k.isspace() == ' ' for k, c in zip(key, word)):
                    count += 1
        except Exception as e:
            raise RuntimeError(f"Error during lookup: {e}")
if __name__ == '__main__':
    dictionary = WordDictionary()
    sample_words = ["apple", "banana", "cherry"]
    for w in sample_words:
        try:
            dictionary.add_word(w)
        except Exception as e:
            print(f"Error adding '{w}': {e}")
    test_pattern = "app.."
    result = dictionary.search(test_pattern)
    count_result = dictionary.get_count("apple")
    if not isinstance(result, bool):
        raise TypeError("Search must return a boolean")
    print(f"Pattern search '{test_pattern}': {result}")
    print(f"Word count for 'apple': {count_result}")