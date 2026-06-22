import threading

class ThreadSafeAverageCalculator:
    def __init__(self):
        self.lock = threading.Lock()
        self.total_sum = 0
        self.count = 0

    def add(self, value):
        with self.lock:
            self.total_sum += value
            self.count += 1

    def get_average(self) -> float:
        with self.lock:
            if self.count == 0:
                return 0.0
            return self.total_sum / self.count

if __name__ == '__main__':
    calculator = ThreadSafeAverageCalculator()
    calculator.add(10)
    calculator.add(20)
    calculator.add(30)
    print(calculator.get_average())