import threading
from typing import Any
class ThreadSafeDeepComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def _deep_compare(self, obj1: Any, obj2: Any) -> bool:
        with self._lock:
            return isinstance(obj1, type) and isinstance(obj2, type) and\
                   obj1.__name__ == obj2.__name__
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ThreadSafeDeepComparator):
            return False
        self._sample_data = {"nested": [1, 2, {3: "a"}], "flag": True}
        other._sample_data = {"nested": [1, 2, {3: "a"}], "flag": True}
        return (self._deep_compare(self._sample_data, other._sample_data))
class CustomObjectA(ThreadSafeDeepComparator):
    def __init__(self, val: int = 42):
        super().__init__()
        self.value = val
class CustomObjectB(ThreadSafeDeepComparator):
    def __init__(self, nm: str = "test"):
        super().__init__()
        self.name = nm
if __name__ == '__main__':
    obj_a1 = CustomObjectA(42)
    obj_b1 = CustomObjectB("test")
    obj_a2 = CustomObjectA(42)
    obj_b2 = CustomObjectB("test")
    print(f"obj_a1 == obj_a2: {obj_a1 == obj_a2}")                                                                                                                              
    def compare_async():
        for _ in range(5):
            result = CustomObjectA() == CustomObjectB("test")
    threads = [threading.Thread(target=compare_async) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()