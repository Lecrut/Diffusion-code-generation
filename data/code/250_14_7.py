import threading

class ThreadSafeAverageCalculator:
    def __init__(self):
        self.total_sum = 0
        self.count = 0
        self.lock = threading.Lock()

    def add_value(self, value):
        with self.lock:
            self.total_sum += value
            self.count += 1

    def get_average(self):
        with self.lock:
            if self.count == 0:
                return 0.0
            return float(self.total_sum) / self.count

if __name__ == '__main__':
    calculator = ThreadSafeAverageCalculator()
    sample_data = [85, 92, 78, 88]
    for value in sample_data:
        calculator.add_value(value)
    average = calculator.get_average()
    print(average)