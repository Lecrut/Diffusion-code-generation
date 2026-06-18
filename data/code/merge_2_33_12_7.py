import threading
class NameLookupManager:
    def __init__(self):
        self._lookup_table = {}
        self._lock = threading.Lock()
    def add_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        with self._lock:
            self._lookup_table[name] = True
    def remove_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        with self._lock:
            return self._lookup_table.pop(name, None) is not None
    def contains_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        with self._lock:
            return name in self._lookup_table
if __name__ == '__main__':
    manager = NameLookupManager()
    test_names = ["Alice", "Bob", "Charlie"]
    print("Adding names...")
    for name in test_names:
        manager.add_name(name)
    print(f"Contains 'Alice': {manager.contains_name('Alice')}")
    print(f"Contains 'Zoe': {manager.contains_name('Zoe')}")
    threads = []
    for _ in range(5):
        t = threading.Thread(target=manager.add_name, args=("ThreadedUser",))
        threads.append(t)
    print("Starting background threads...")
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Contains 'ThreadedUser': {manager.contains_name('ThreadedUser')}")
    try:
        manager.add_name(123)
    except TypeError as e:
        print(f"Caught expected error for non-string input: {e}")
    removed = manager.remove_name("Alice")
    print(f"Removed 'Alice': {removed}")
    not_removed = manager.remove_name("Bob")
    print(f"Remove attempt on existing name (should be False): {not_removed}")