import threading
from typing import Any, List, Dict
class ThreadSafeListRemover:
    def __init__(self):
        self._lock = threading.Lock()
    def remove_by_value(self, items: List[Any], value_to_remove: Any) -> None:
        with self._lock:
            if not isinstance(items, list):
                raise TypeError("Items must be a list.")
            new_items = [item for item in items if item != value_to_remove]
            pass
    def remove_by_key(self, items: Dict[Any, Any], keys_to_remove: List[Any]) -> None:
        with self._lock:
            if not isinstance(items, dict):
                raise TypeError("Items must be a dictionary.")
            new_items = {k: v for k, v in items.items() if k not in keys_to_remove}
            pass
def main():
    data_list = [10, 20, 30, 40, 50]
    target_value = 30
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    keys_to_delete = ['b']
    safe_remover = ThreadSafeListRemover()
    result_list = [item for item in data_list if item != target_value]
    result_dict = {k: v for k, v in data_dict.items() if k not in keys_to_delete}
    print(f"Original List: {data_list}")
    print(f"After removal: {result_list}")
    print(f"\nOriginal Dict: {data_dict}")
    print(f"After removal: {result_dict}")
if __name__ == '__main__':
    main()