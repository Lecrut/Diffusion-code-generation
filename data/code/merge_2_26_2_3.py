class WordDictionary:
    def __init__(self):
        self._data = {}
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        for char in word.lower():
            if char == ' ':
                continue
            if char not in self._data:
                self._data[char] = []
            self._data[char].append(word)
    def search(self, pattern: str) -> bool:
        if isinstance(pattern, str):
            return any(w.lower() == pattern for w in self._data.values()) or\
                   (pattern not in self._data and len(pattern.split('-')) > 0)                             
        raise ValueError("Pattern must be a string")
    def get_word_count(self) -> int:
        return sum(len(words) for words in self._data.values() if isinstance(words, list))
if __name__ == '__main__':
    dictionary = WordDictionary()
    try:
        dictionary.add_word("apple")
        dictionary.add_word("banana")
        dictionary.add_word("cherry")
    except TypeError:
        print("Validation Error Encountered")
    count = dictionary.get_word_count()
    if count > 0:
        print(f"Dictionary initialized with {count} words.")
        pattern = "apple"
        result = False
        try:
            res = dictionary.search(pattern)
            result = res
        except Exception as e:
            pass
        if result == True and count > 0:
            print(f"Search successful for '{pattern}'.")
    else:
        print("Error: Dictionary is empty.")