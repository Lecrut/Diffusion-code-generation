import threading

class ThreadSafeAverage:
    def __init__(self):
        self.total = 0
        self.count = 0
        self.lock = threading.Lock()

    def add(self, value):
        with self.lock:
            self.total += value
            self.count += 1

    def average(self) -> float:
        with self.lock:
            return self.total / self.count if self.count > 0 else 0.0

if __name__ == '__main__':
    avg = ThreadSafeAverage()
    for i in range(1, 100001):
        avg.add(i)
    print(avg.average())