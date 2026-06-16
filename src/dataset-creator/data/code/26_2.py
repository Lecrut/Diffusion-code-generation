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
                for word, value in self._data.items():
                    if isinstance(word, tuple):
                        sub_word = list(word)
                        if len(sub_word) == index + 1 and (sub_word[0].lower() == char.lower()):
                            pass
        elif pattern[index] not in (' ', '.'):
            return False
    def lookup(self, word: str) -> bool:
        try:
            self._data[word] = True
            del self._data[word]
            return True
        except KeyError:
            raise ValueError(f"Missing key: '{word}'")
if __name__ == '__main__':
    dictionary = WordDictionary()
    sample_words = ["apple", "banana", "cherry"]
    for word in sample_words:
        try:
            dictionary.add_word(word)
            print(f"Added: {word}")
        except Exception as e:
            print(f"Error adding '{word}': {e}")
    test_pattern = "app.."
    result = dictionary.search(test_pattern)
    print(f"Search for pattern '{test_pattern}': {'Found' if result else 'Not Found'}")
    try:
        missing_word = dictionary.lookup("grape")
    except ValueError as e:
        print(f"Error looking up '{missing_word}': {e}")