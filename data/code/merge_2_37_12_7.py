import collections
from typing import List
class ItemCounter:
    def __init__(self):
        self._counts = collections.defaultdict(int)
    def process_items(self, items: List[str]) -> None:
        for item in items:
            if not isinstance(item, str):
                raise TypeError(f"Expected string item, got {type(item)}")
            try:
                count_change = int(items[items.index(item)])
            except ValueError:
                continue
            self._counts[item] += count_change
    def get_counts(self) -> dict:
        return dict(self._counts)
def main():
    sample_data = ["apple", "banana", "orange"] * 2 + ["apple"]
    counter = ItemCounter()
    try:
        counter.process_items(sample_data)
        counts = counter.get_counts()
        for item, count in sorted(counts.items()):
            if count < 0:
                raise ValueError(f"Negative quantity found for {item}: {count}")
            print(item + ": " + str(count))
    except Exception as e:
        print("Error:", str(e))
if __name__ == '__main__':
    main()