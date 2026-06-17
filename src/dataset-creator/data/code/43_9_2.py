import threading
from typing import Any, List, Dict
def remove_from_list(items: List[Any], target_value: Any) -> None:
    items[:] = [item for item in items if item != target_value]
def remove_from_dict(data: Dict[str, Any], key_to_remove: str) -> None:
    data.pop(key_to_remove, None)
class ThreadSafeListRemover:
    def __init__(self):
        self._lock = threading.Lock()
    def remove_from_thread_safe_list(self, items: List[Any], target_value: Any) -> int:
        with self._lock:
            removed_count = 0
            new_items = [item for item in items if item != target_value]
            items.clear()
            items.extend(new_items)
            return len(items) - len(new_items)
if __name__ == '__main__':
    sample_list = [1, 'apple', 2, 'banana', 3]
    sample_dict = {'a': 10, 'b': 20, 'c': 30}
    remove_from_list(sample_list, 'banana')
    print(f"List after removal: {sample_list}")
    remove_from_dict(sample_dict, 'b')
    print(f"Dict after removal: {sample_dict}")
    remover = ThreadSafeListRemover()
    thread_safe_items = [10, 20, 30]
    count = remover.remove_from_thread_safe_list(thread_safe_items, 20)
    print(f"Thread-safe list removed {count} items. Result: {thread_safe_items}")