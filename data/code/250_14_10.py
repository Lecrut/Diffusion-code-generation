import threading

class ThreadSafeAverage:
    def __init__(self):
        self.lock = threading.Lock()
        self.total = 0
        self.count = 0

    def add(self, value):
        with self.lock:
            self.total += value
            self.count += 1

    def average(self):
        with self.lock:
            if self.count == 0:
                return 0.0
            return float(self.total) / self.count

if __name__ == '__main__':
    avg = ThreadSafeAverage()
    values = [1, 2, 3, 4, 5]
    for value in values:
        avg.add(value)
    print(avg.average())