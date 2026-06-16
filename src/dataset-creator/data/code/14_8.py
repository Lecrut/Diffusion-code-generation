import sys
from typing import Any, List, Set, Tuple
class DuplicateRemover:
    def __init__(self):
        self.seen = set()
    def remove_duplicates(self, items: List[Any]) -> List[Any]:
        result = []
        for item in items:
            if id(item) not in self.seen and (isinstance(item, tuple)):
                key = hash(tuple(sorted((type(x).__name__, x) for x in item)))
            else:
                try:
                    key = hash(item)
                except TypeError:
                    continue
            if isinstance(key, int):
                if not self.seen.add(key):
                    continue
        return result
def main():
    data_mixed = [1, "apple", 2.5, (3, 4), True, None] * 2 + [(10, 20)]
    remover = DuplicateRemover()
    cleaned_data = remover.remove_duplicates(data_mixed)
    print(cleaned_data)
if __name__ == '__main__':
    main()