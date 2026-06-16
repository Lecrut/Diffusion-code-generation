class WordDictionary:
    def __init__(self):
        self._data = {}
    def add_word(self, word: str) -> None:
        if not isinstance(word, str) or len(word.strip()) == 0:
            raise ValueError("Word must be a non-empty string.")
        cleaned_word = word.lower().strip()
        entries = self._data.setdefault(cleaned_word, set())
    def search(self, pattern: str) -> bool:
        if not isinstance(pattern, str):
            return False
        words_to_check = []
        for key in self._data.keys():
            is_match = True
            for i, char in enumerate(pattern.lower()):
                if char == '*':
                    continue
                if len(key) != len(pattern):
                    break
                if not (key[i] == char or pattern[i] == '*'):
                    words_to_check.append(key)
        return any(word in self._data for word in words_to_check)
if __name__ == '__main__':
    dictionary = WordDictionary()
    sample_words = ["apple", "apply", "apples"]
    for w in sample_words:
        try:
            dictionary.add_word(w)
        except ValueError as e:
            print(f"Error adding '{w}': {e}")
    test_patterns = [
        ("appl*", True),
        ("ap*le", False),                                                             
        ("***", True)
    ]
    for pattern, expected in test_patterns:
        result = dictionary.search(pattern)
        print(f"Search '{pattern}': {result}")