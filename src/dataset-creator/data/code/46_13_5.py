import threading
class ThreadSafeSetDifference:
    def __init__(self):
        self.lock = threading.Lock()
    def symmetric_difference(self, set_a, set_b):
        with self.lock:
            return (set_a - set_b) | (set_b - set_a)
if __name__ == '__main__':
    calculator = ThreadSafeSetDifference()
    result = calculator.symmetric_difference({1, 2, 3}, {3, 4, 5})
    print(result)