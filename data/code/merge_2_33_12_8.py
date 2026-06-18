import threading
from typing import Dict
class NameLookupManager:
    def __init__(self) -> None:
        self._lookup_table: Dict[str, str] = {}
        self._lock = threading.Lock()
    def add_name(self, name: str, value: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        with self._lock:
            if name in self._lookup_table:
                return False
            try:
                self._lookup_table[name] = value
                return True
            except Exception as e:
                print(f"Error adding entry for '{name}': {e}")
                raise
    def get_name(self, name: str) -> str | None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        with self._lock:
            return self._lookup_table.get(name)
    def remove_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        with self._lock:
            was_present = name in self._lookup_table
            try:
                del self._lookup_table[name]
                return True
            except KeyError as e:
                print(f"Entry for '{name}' not found. {e}")
                raise
    def size(self) -> int:
        with self._lock:
            return len(self._lookup_table)
if __name__ == '__main__':
    manager = NameLookupManager()
    sample_data = [
        ("Alice", "123-456-7890"),
        ("Bob", "098-765-4321"),
        ("Charlie", "555-123-4567")
    ]
    for name, value in sample_data:
        manager.add_name(name, value)
    print(f"Total entries added: {manager.size()}")
    test_queries = ["Alice", "Bob"]
    results = []
    for n in test_queries:
        try:
            result = manager.get_name(n)
            if result is not None:
                results.append(f"{n}: {result}")
            else:
                print(f"Name '{n}' not found.")
        except Exception as e:
            print(f"Error querying for '{n}': {e}")
    try:
        manager.remove_name("Bob")
        remaining = [name for name, _ in sample_data if name != "Charlie"]
        print(f"After removal of Bob. Remaining expected count logic applied.")
        alice_val = manager.get_name("Alice")
        bob_val = manager.get_name("Bob")
        assert alice_val == "123-456-7890", "Alice's data should remain."
        assert bob_val is None, "Bob's data should be removed."
    except AssertionError as e:
        print(f"Assertion failed during verification: {e}")