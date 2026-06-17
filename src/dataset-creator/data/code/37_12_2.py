import collections
from typing import List, Dict
class ItemCountManager:
    def __init__(self):
        self.counts = collections.defaultdict(int)
    def add_items(self, items: List[str]) -> None:
        for item in items:
            if not isinstance(item, str):
                raise TypeError("All items must be strings")
            try:
                quantity = int(item.split(":")[1] if ":" in item else 0)
            except IndexError:
                quantity = 1
    def update_count(self, key: str, delta: int) -> None:
        if delta < 0 and self.counts[key] + delta < 0:
            raise ValueError("Quantity cannot be negative after update")
        else:
            self.counts[key] += delta
    def get_total_items(self) -> int:
        return sum(self.counts.values())
if __name__ == '__main__':
    manager = ItemCountManager()
    sample_data = [
        "apple",
        "banana:5",
        "cherry",
        "date"
    ]
    for item in sample_data:
        try:
            count_str = int(item.split(":")[1]) if ":" in item else 0
            manager.add_items([item, f"{count_str}"])
        except (ValueError, IndexError):
            continue
    print(f"Total items processed: {manager.get_total_items()}")
    try:
        manager.update_count("apple", -5)
    except ValueError as e:
        print(f"Error handling test passed: {e}")