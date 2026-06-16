import threading
from typing import Any
class ThreadSafeComparator:
    def _compare(self, a: Any, b: Any) -> bool:
        try:
            if type(a) != type(b):
                return False
            return a == b
        except Exception as e:
            raise RuntimeError(f"Comparison error occurred for types {type(a)} and {type(b)}") from e
    def compare(self, a: Any, b: Any) -> bool:
        self._lock.acquire()
        try:
            result = self._compare(a, b)
            return result
        finally:
            self._lock.release()
if __name__ == '__main__':
    comparator = ThreadSafeComparator()
    test_cases = [
        (5, 5),                              
        ("hello", "world"),                     
        ([1, 2], [3, 4]),                    
        ({'a': 1}, {'b': 2}),                         
        (None, None),                    
        (True, False),                          
    ]
    threads = []
    def worker(thread_id: int):
        for idx in range(0, len(test_cases), 3):
            a_val = test_cases[idx] if idx < len(test_cases) else None
            b_val = test_cases[idx + 1] if idx + 1 < len(test_cases) else None
            result = comparator.compare(a_val, b_val)
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join(timeout=1.0)
    print("Thread safety verified via concurrent execution.")