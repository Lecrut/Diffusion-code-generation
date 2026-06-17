import threading
from typing import List, Dict, Any
def remove_from_list(items: List[Any], target_value: Any) -> None:
    items[:] = [item for item in items if item != target_value]
def safe_remove_dict_items(data: Dict[str, Any], keys_to_remove: List[str]) -> None:
    lock = threading.Lock()
    def _remove():
        with lock:
            for key in list(keys_to_remove):                                                                   
                data.pop(key, None)
    threads = [threading.Thread(target=_remove)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b', 5]
    target_to_remove = 3
    remove_from_list(sample_list, target_to_remove)
    sample_dict = {'x': 10, 'y': 20, 'z': 30}
    keys_to_delete = ['x']
    safe_remove_dict_items(sample_dict, keys_to_delete)