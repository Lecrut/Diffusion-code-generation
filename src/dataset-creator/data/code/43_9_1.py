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
    threads = []
    for i in range(0, len(keys_to_remove), 2):
        chunk_keys = keys_to_remove[i:i+2]
        t = threading.Thread(target=_remove, args=(data, list(chunk_keys)))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', 40]
    target_to_remove = 30
    remove_from_list(sample_list, target_to_remove)
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    keys_to_delete = ['a']
    safe_remove_dict_items(sample_dict, keys_to_delete)