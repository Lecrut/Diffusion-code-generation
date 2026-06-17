import threading
class ThreadSafeSet:
    def __init__(self):
        self._data = set()
        self._lock = threading.Lock()
    def add(self, item):
        with self._lock:
            self._data.add(item)
    def remove(self, item):
        with self._lock:
            if item in self._data:
                self._data.remove(item)
    def symmetric_difference(self, other_set):
        result = set()
        for item in self._data.symmetric_difference(other_set._data):
            result.add(item)
        return result
if __name__ == '__main__':
    ts1 = ThreadSafeSet()
    ts2 = ThreadSafeSet()
    sample_values_1 = {1, 3, 5}
    for val in sample_values_1:
        ts1.add(val)
    sample_values_2 = {2, 4, 6}
    for val in sample_values_2:
        ts2.add(val)
    diff_set = ts1.symmetric_difference(ts2)
    print(diff_set)