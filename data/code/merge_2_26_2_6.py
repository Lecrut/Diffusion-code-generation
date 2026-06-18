class WordDictionary:
    def __init__(self):
        self._dictionary = {}
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Input must be a string.")
        clean_word = ' '.join(word.split())
        try:
            int(clean_word)
        except ValueError:
            self._dictionary[clean_word] = True
    def search(self, pattern: str) -> bool:
        if not isinstance(pattern, str):
            raise TypeError("Input must be a string.")
        clean_pattern = ' '.join(pattern.split())
        return any(clean_key == clean_pattern or all(c in w for c in clean_pattern[:len(clean_word)]) 
                  for clean_key, _ in self._dictionary.items() if len(w) > 0 and set(clean_key).issubset(set(w)))
    def __contains__(self, word: str) -> bool:
        return any(word == key or all(c in k for c in word[:len(k)]) 
                  for key in self._dictionary.keys())
if __name__ == '__main__':
    d = WordDictionary()
    d.add_word("apple")
    d.add_word("application")
    if "apple" in d:
        print(True)
    else:
        raise KeyError("'apple' not found.")