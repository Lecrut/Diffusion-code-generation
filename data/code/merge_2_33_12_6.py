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
    def get_names(self) -> list[str]:
        return sorted(list(self._lookup_table.keys()))
    def remove_name(self, name: str) -> bool:
        with self._lock:
            was_present = name in self._lookup_table
            del self._lookup_table[name]
            return was_present
    def __len__(self) -> int:
        with self._lock:
            return len(self._lookup_table)
if __name__ == '__main__':
    manager = NameLookupManager()
    test_names = ["Alice", "Bob", "Charlie"]
    print("Adding names:", ", ".join(test_names))
    for name in test_names:
        try:
            if not manager.add_name(name):
                raise ValueError(f"Failed to add '{name}'")
        except Exception as e:
            print(f"Error adding {name}: {e}")
    print("Retrieved names:", ", ".join(manager.get_names()))
    threads = []
    num_threads = 4
    def worker(thread_id, name):
        try:
            manager.add_name(name)
        except Exception as e:
            print(f"Thread {thread_id} error: {e}")
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i, f"Worker_{i}_Name"))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Final count:", len(manager))
    print("All names sorted:")
    for name in manager.get_names():
        print(f"  - {name}")