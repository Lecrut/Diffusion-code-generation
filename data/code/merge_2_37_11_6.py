import threading
class InventoryManager:
    def __init__(self) -> None:
        self._counts = {}
        self._lock = threading.Lock()
    def increment(self, item_id: str, amount: int = 1) -> None:
        with self._lock:
            if not isinstance(amount, int):
                raise TypeError("Amount must be an integer")
            current_count = self._counts.get(item_id, 0)
            new_count = current_count + amount
            if new_count < 0:
                raise ValueError(f"Cannot decrement {item_id} below zero")
            self._counts[item_id] = new_count
    def decrement(self, item_id: str, amount: int = 1) -> None:
        with self._lock:
            current_count = self._counts.get(item_id, 0)
            if current_count < amount:
                raise ValueError(f"Insufficient stock for {item_id}")
            new_count = current_count - amount
            self._counts[item_id] = new_count
    def get(self, item_id: str) -> int:
        with self._lock:
            return self._counts.get(item_id, 0)
    def reset_inventory(self) -> None:
        with self._lock:
            self._counts.clear()
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.increment("apple", 5)
    inventory.increment("banana", 3)
    print(f"Apple count: {inventory.get('apple')}")
    print(f"Banana count: {inventory.get('banana')}")
    inventory.decrement("apple", 2)
    print(f"Updated Apple count: {inventory.get('apple')}")
    inventory.reset_inventory()
    print(f"After reset - Banana count: {inventory.get('banana')}")