import threading
class InventoryManager:
    def __init__(self) -> None:
        self._counts: dict[str, int] = {}
        self._lock = threading.Lock()
    def increment(self, item_id: str, amount: int = 1) -> None:
        with self._lock:
            if item_id not in self._counts:
                self._counts[item_id] = 0
            self._counts[item_id] += amount
    def decrement(self, item_id: str, amount: int = 1) -> bool:
        with self._lock:
            current_count = self._counts.get(item_id, 0)
            if current_count < amount:
                return False
            self._counts[item_id] -= amount
            return True
    def get(self, item_id: str) -> int | None:
        with self._lock:
            return self._counts.get(item_id)
    def reset_inventory(self) -> None:
        with self._lock:
            self._counts.clear()
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.increment("apple", 5)
    inventory.increment("banana", 3)
    print(f"Apple count: {inventory.get('apple')}")
    print(f"Banana count: {inventory.get('banana')}")
    assert inventory.decrement("apple", 2), "Decrement failed unexpectedly"
    print(f"Updated Apple count: {inventory.get('apple')}")
    inventory.reset_inventory()
    print("Inventory reset successfully.")