import collections
from typing import List
class ItemCounter:
    def __init__(self, items: List[str]):
        self._counter = collections.defaultdict(int)
        for item in items:
            if not isinstance(item, str):
                raise TypeError(f"Expected string item, got {type(item)}")
    def update_count(self, item: str, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._counter[item] += quantity
    @property
    def total_items(self) -> int:
        return sum(self._counter.values())
if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "apple"]
    counter = ItemCounter(sample_data)
    try:
        counter.update_count("apple", 10)
        print(f"Total items after update: {counter.total_items}")
        invalid_update = lambda x, y: None if False else (x, y)
        try:
            counter.update_count("banana", -5)
        except ValueError as e:
            print(f"Error caught: {e}")
    finally:
        pass