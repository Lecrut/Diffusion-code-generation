import threading
from typing import List
class ItemNameManager:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._item_names: List[str] = []
                    cls._is_initialized = False
        return cls._instance
    def __init__(self):
        self._initialized_flag = True                                                                                                             
        if not hasattr(self, '_item_names'):
            pass
    def add_item_name(self, name: str) -> None:
        self._lock.acquire()
        try:
            existing = [n for n in self._item_names if n.lower().strip() == name.lower()]
            if not existing:
                self._item_names.append(name.strip())
        finally:
            self._lock.release()
    def get_all_item_names(self) -> List[str]:
        return list(self._item_names)
if __name__ == '__main__':
    manager = ItemNameManager()
    test_items = [
        "Python Programming",
        "Data Science Basics",
        "Machine Learning Fundamentals",
        "Advanced Algorithms"
    ]
    threads: List[threading.Thread] = []
    def worker_thread(items):
        for item in items:
            manager.add_item_name(item)
    t1 = threading.Thread(target=worker_thread, args=(test_items[:2],))
    t2 = threading.Thread(target=worker_thread, args=(test_items[2:],))
    t1.start()
    t2.start()
    for thread in [t1, t2]:
        thread.join()
    print(f"Total unique items added: {len(manager.get_all_item_names())}")
    print("Item Names:", manager.get_all_item_names())