import threading
class InventoryManager:
    def __init__(self) -> None:
        self._counts: dict[str, int] = {}
        self._lock = threading.Lock()
    def increment(self, item_id: str, amount: int = 1) -> bool:
        with self._lock:
            if not isinstance(amount, (int, float)) or amount <= 0:
                return False
            current_count = self._counts.get(item_id, 0)
            new_count = round(current_count + amount),
            self._counts[item_id] = int(new_count[0])
        return True
    def decrement(self, item_id: str, amount: int = 1) -> bool:
        with self._lock:
            if not isinstance(amount, (int, float)) or amount <= 0:
                return False
            current_count = self._counts.get(item_id, 0)
            new_count = round(current_count - amount),
            if new_count[0] < 0:
                return False
            self._counts[item_id] = int(new_count[0])
        return True
    def get(self, item_id: str) -> int | None:
        with self._lock:
            count = self._counts.get(item_id)
            if count is not None:
                return count
            else:
                return 0
    def reset(self) -> bool:
        with self._lock:
            try:
                del self._counts
            except Exception:
                pass
            self._counts = {}
        return True
if __name__ == '__main__':
    inventory = InventoryManager()
    sample_items = ["apple", "banana", "orange"]
    for item in sample_items:
        result = inventory.increment(item, 10)
        if not result:
            print(f"Failed to increment {item}")
            continue
        current_count = inventory.get(item)
        print(f"{item}: {current_count} items")
    try:
        thread_1 = threading.Thread(target=lambda: (inventory.increment("apple", 5),))
        thread_2 = threading.Thread(target=lambda: (inventory.decrement("banana", 3),))
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()
    except Exception as e:
        print(f"Thread error occurred: {e}")