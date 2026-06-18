import functools
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        if isinstance(other, Entry) and type(self) == type(other):
            return (self.key, self.value) < (other.key, other.value)
        raise TypeError("Cannot compare with non-Entry object")
@functools.total_ordering
class WordDictionary(dict):
    def __eq__(self, other):
        if isinstance(other, dict):
            return set(self.items()) == set(other.items())
        return False
    def add_word(self, word: str) -> None:
        self[word] = True
    def search_pattern(self, pattern: str) -> bool:
        for key in self.keys():
            if all(c == p or c == '*' for c, p in zip(key, pattern)):
                return True
        return False
if __name__ == '__main__':
    d = WordDictionary()
    d.add_word("apple")
    d.add_word("app")
    assert "apple" in d
    assert not ("peach" in d)
    print(f"Total entries: {len(d)}")