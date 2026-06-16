import functools
class WordEntry:
    def __init__(self, word):
        self.word = word
    def __lt__(self, other):
        return isinstance(other, WordEntry) and (self.word < other.word or 
                                                  (self.word == other.word and id(self) < id(other)))
@functools.total_ordering
class EfficientWordDict(dict):
    pass
if __name__ == '__main__':
    data = {
        'apple': WordEntry('banana'),
        'cat': WordEntry('dog'),
        'elephant': WordEntry('ant')
    }
    print("Initial dictionary:", dict(data))
    new_entry = EfficientWordDict()
    new_entry['zebra'] = WordEntry('monkey')
    data.update(new_entry)
    print("After update:", {k: v.word for k, v in data.items()})