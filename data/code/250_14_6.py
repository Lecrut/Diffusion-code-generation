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

    def get_average(self) -> float:
        with self.lock:
            if self.count == 0:
                return 0.0
            return self.total / self.count

if __name__ == '__main__':
    avg = ThreadSafeAverage()
    for i in range(1, 100001):
        avg.add(i)
    print(avg.get_average())