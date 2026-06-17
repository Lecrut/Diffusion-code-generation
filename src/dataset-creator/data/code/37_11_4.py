import threading
class InventoryManager:
    def __init__(self) -> None:
        self._counts: dict[str, int] = {}
        self._lock = threading.Lock()
    def increment(self, item_name: str, amount: int = 1) -> None:
        with self._lock:
            if item_name not in self._counts:
                self._counts[item_name] = 0
            self._counts[item_name] += amount
    def decrement(self, item_name: str, amount: int = 1) -> bool:
        with self._lock:
            current_count = self._counts.get(item_name, 0)
            if current_count < amount:
                return False
            self._counts[item_name] -= amount
            return True
    def get_count(self, item_name: str) -> int:
        with self._lock:
            return self._counts.get(item_name, 0)
    def reset_inventory(self) -> None:
        with self._lock:
            self._counts.clear()
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.increment("apple", 5)
    inventory.increment("banana", 3)
    print(f"Apple count: {inventory.get_count('apple')}")
    print(f"Banana count: {inventory.get_count('banana')}")
    result = inventory.decrement("apple", 2)
    if result:
        print(f"After decrement, Apple count is now {inventory.get_count('apple')}")
    else:
        print("Insufficient stock.")
    inventory.reset_inventory()
    print("Inventory reset successfully.")