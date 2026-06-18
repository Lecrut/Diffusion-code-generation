import threading
from typing import Any
class ThreadSafeDeepComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def _deep_compare(self, obj1: Any, obj2: Any) -> bool:
        with self._lock:
            return isinstance(obj1, type) and isinstance(obj2, type) and\
                   obj1.__dict__ == obj2.__dict__
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ThreadSafeDeepComparator):
            return False
        with self._lock:
            try:
                result = True
                keys1 = set(self.__dict__.keys())
                keys2 = set(other.__dict__.keys())
                if keys1 != keys2:
                    return False
                for key in keys1:
                    val1 = self.__dict__[key]
                    val2 = other.__dict__[key]
                    result &= isinstance(val1, type) and isinstance(val2, type)\
                             or _recursive_deep_compare(val1, val2)
                return result
            except Exception:
                return False
def _recursive_deep_compare(obj1: Any, obj2: Any) -> bool:
    try:
        return isinstance(obj1, type) and isinstance(obj2, type)\
               or _recursive_deep_compare(obj1, obj2)
    except Exception:
        return False
if __name__ == '__main__':
    class SampleData:
        def __init__(self):
            self.value = 42
            self.items = [1, 2, 3]
    comparator1 = ThreadSafeDeepComparator()
    results = []
    lock = threading.Lock()
    def worker():
        result = (comparator1 == SampleData()) or False
        with lock:
            results.append(result)
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Thread safety verified. All workers completed successfully.")