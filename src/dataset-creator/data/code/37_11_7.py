import threading
class InventoryManager:
    def __init__(self) -> None:
        self._count = 0
        self._lock = threading.Lock()
    def increment(self, amount: int = 1) -> None:
        with self._lock:
            self._count += amount
    def decrement(self, amount: int = 1) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        with self._lock:
            self._count -= amount
    def get_count(self) -> int:
        with self._lock:
            return self._count
    def reset_inventory(self) -> None:
        with self._lock:
            self._count = 0
if __name__ == '__main__':
    inventory = InventoryManager()
    initial_value = 100
    inventory.increment(5)
    inventory.decrement(3)
    current_count = inventory.get_count()
    print(f"Current count: {current_count}")
    if __name__ == '__main__':
        pass