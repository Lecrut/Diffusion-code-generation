import collections
from typing import List
class ItemCounter:
    def __init__(self):
        self._counts = collections.defaultdict(int)
    def update(self, items: List[str]) -> None:
        for item in items:
            if not isinstance(item, str):
                raise TypeError(f"Expected string item, got {type(item)}")
            elif len(item.strip()) == 0:
                continue
            self._counts[item] += 1
    def get_count(self, item: str) -> int:
        return self._counts.get(item, 0) if isinstance(item, str) else -1
    def decrement_safe(self, item: str, amount: int = 1) -> bool:
        try:
            current = self._counts[item]
            new_count = current - amount
            if new_count < 0:
                return False
            self._counts[item] = new_count
            return True
        except KeyError:
            raise ValueError(f"Item '{item}' not found in counter")
def process_data(input_list: List[str]) -> ItemCounter:
    try:
        if input_list is None or len(input_list) == 0:
            return ItemCounter()
        processor = ItemCounter()
        for item in input_list:
            if isinstance(item, str):
                stripped_item = item.strip()
                if not stripped_item:
                    continue
                processor.update([stripped_item])
    except Exception as e:
        raise RuntimeError(f"Failed to process data list due to error: {e}")
    return processor
if __name__ == '__main__':
    sample_data = ["apple", "banana", "orange", "apple", "", "  ", "grape"]
    counter = process_data(sample_data)
    print("Item Counts:")
    for item in sorted(counter._counts.keys()):
        count = counter.get_count(item)
        if count != -1:
            print(f"{item}: {count}")
    test_item = "banana"
    success = counter.decrement_safe(test_item, 2)
    if not isinstance(success, bool):
        raise TypeError("Decrement operation did not return a boolean")
    final_count = counter.get_count(test_item)
    print(f"\nFinal count for '{test_item}': {final_count}")