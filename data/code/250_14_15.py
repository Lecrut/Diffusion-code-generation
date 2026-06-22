import threading

class ThreadSafeAverageCalculator:
    def __init__(self):
        self._total = 0.0
        self._count = 0
        self._lock = threading.Lock()

    def add(self, value):
        with self._lock:
            self._total += value
            self._count += 1

    def average(self) -> float:
        with self._lock:
            if self._count == 0:
                return 0.0
            return self._total / self._count

if __name__ == '__main__':
    calculator = ThreadSafeAverageCalculator()
    values = [85, 92, 78, 88]
    for value in values:
        calculator.add(value)
    avg = calculator.average()
    print(avg)