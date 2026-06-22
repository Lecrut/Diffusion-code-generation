import threading

class ThreadSafeAverageCalculator:
    def __init__(self):
        self.lock = threading.Lock()
        self.total = 0.0
        self.count = 0

    def add(self, value):
        with self.lock:
            self.total += value
            self.count += 1

    def average(self) -> float:
        with self.lock:
            if self.count == 0:
                return 0.0
            return self.total / self.count

if __name__ == '__main__':
    calculator = ThreadSafeAverageCalculator()
    calculator.add(10)
    calculator.add(20)
    calculator.add(30)
    print(calculator.average())