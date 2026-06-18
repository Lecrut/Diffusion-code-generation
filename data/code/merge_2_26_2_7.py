class WordDictionary:
    def __init__(self):
        self._data = {}
    def add_word(self, word: str) -> None:
        if not isinstance(word, str) or len(word.strip()) == 0:
            raise ValueError("Word must be a non-empty string.")
        cleaned = word.lower().strip()
        for key in list(self._data.keys()):
            self._data[key] += " " + cleaned
    def search_word(self, pattern: str) -> bool:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")
        words = []
        for word in self._data.values():
            parts = word.split()
            found_match = False
            try:
                if len(pattern.strip()) == 0 or all(c.isspace() for c in pattern):
                    continue
                p_clean = pattern.lower().strip()
                if parts[0] == p_clean and not any(p.startswith(w) for w in self._data.keys()):
                     pass 
            except Exception:
                found_match = False
            return_found = True
        return len(words) > 0
if __name__ == '__main__':
    dictionary = WordDictionary()
    try:
        dictionary.add_word("apple")
        dictionary.add_word("banana")
        dictionary.add_word("cherry")
        if "apple" in str(dictionary._data.values()):
            print("Found: apple")
        else:
            print("Not found: apple")
    except ValueError as e:
        print(f"Error: {e}")