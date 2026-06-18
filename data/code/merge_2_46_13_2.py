import threading
class ThreadSafeSetDifference:
    def __init__(self):
        self._lock = threading.Lock()
    def symmetric_difference(self, set_a, set_b):
        with self._lock:
            return (set_a - set_b) | (set_b - set_a)
if __name__ == '__main__':
    calculator = ThreadSafeSetDifference()
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    result = calculator.symmetric_difference(s1, s2)
    print(result)