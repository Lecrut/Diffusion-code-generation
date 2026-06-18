import functools
class WordEntry:
    def __init__(self, word):
        self.word = word
    def __lt__(self, other):
        return isinstance(other, WordEntry) and self.word < other.word
    @property
    def key(self):
        return self.word
@functools.total_ordering
class DictionarySystem(dict):
    pass
if __name__ == '__main__':
    entries = [WordEntry("apple"), WordEntry("banana"), WordEntry("cherry")]
    d = DictionarySystem()
    for entry in entries:
        d[entry.key] = f"Length of {entry.word}: {len(entry.word)}"
    print(list(d.keys()))