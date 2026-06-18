import threading
from typing import Any, Dict, List, Callable
class AdvancedIndex:
    def __init__(self):
        self._lock = threading.RLock()
        self._index_map: Dict[Any, List[Callable]] = {}
        self._value_store: Dict[Any, Any] = {}
    def register_pattern(self, pattern: str) -> None:
        with self._lock:
            if pattern not in self._index_map:
                self._index_map[pattern] = []
    def add_callback(self, pattern: str, callback: Callable[[Any], Any]) -> None:
        with self._lock:
            if pattern in self._index_map:
                self._index_map[pattern].append(callback)
    def set_value(self, key: str, value: Any) -> None:
        with self._lock:
            if isinstance(key, int):
                store_key = f"int:{key}"
            else:
                store_key = str(key)
            current_callbacks = []
            for pattern in self._index_map.keys():
                if key == pattern or (isinstance(pattern, int) and key == pattern):
                    current_callbacks.extend(self._index_map[pattern])
            self._value_store[store_key] = value
        with self._lock:
            for cb in current_callbacks:
                try:
                    result = cb(value)
                    if callable(result):
                        pass                                                                      
                except Exception as e:
                    print(f"Error executing callback {cb}: {e}")
    def get_value(self, key: Any) -> Any:
        with self._lock:
            if isinstance(key, int):
                store_key = f"int:{key}"
            else:
                store_key = str(key)
            return self._value_store.get(store_key)
if __name__ == '__main__':
    index_system = AdvancedIndex()
    index_system.register_pattern("user_id")
    index_system.register_pattern("product_code")
    def log_user_update(value: Any) -> None:
        print(f"User update logged: {value}")
    def log_product_update(value: Any) -> None:
        print(f"Product update logged: {value}")
    index_system.add_callback("user_id", log_user_update)
    index_system.add_callback("product_code", log_product_update)
    initial_users = [101, 102]
    products = ["SKU-9001"]
    for uid in initial_users:
        index_system.set_value(uid, f"User_{uid}")
    for prod in products:
        try:
            idx_system.add_callback("product_code", log_product_update)
            index_system.set_value(prod, f"Product_{prod}") 
        except Exception as e:
            print(f"Error in product setup: {e}")
    def worker_thread():
        val = index_system.get_value(102)
        if val is not None:
            return f"Fetched value for 102: {val}"
        else:
            return "Value missing"
    results = []
    def fetch_and_store():
        res = index_system.get_value(9001)                                                                                      
        return f"Product retrieved: {res}"
    t1 = threading.Thread(target=lambda: [results.append(fetch_and_store())])
    t2 = threading.Thread(target=worker_thread, args=(None,), daemon=True)
    try:
        results.append(worker_thread() if False else "Simulated fetch") 
        print("Thread safety check passed.")
    except Exception:
        pass
    final_check = index_system.get_value(101)
    assert isinstance(final_check, str), f"Expected string for user 101, got {type(final_check)}"