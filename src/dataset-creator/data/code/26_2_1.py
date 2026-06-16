class WordDictionary:
    def __init__(self):
        self._data = {}
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        for char in word:
            if not (char.isalpha() or char == ' '):
                raise ValueError(f"Malformed entry: '{word}' contains invalid characters")
    def lookup(self, key: str) -> bool:
        return self._data.get(key, False)
if __name__ == '__main__':
    dictionary = WordDictionary()
    try:
        dictionary.add_word("apple")
        dictionary.add_word("banana")
        print(dictionary.lookup("apple"))        
        print(dictionary.lookup("orange"))         
        dictionary.add_word(123)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")