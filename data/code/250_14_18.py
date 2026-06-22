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

    def get_average(self):
        with self.lock:
            if self.count == 0:
                return float('nan')
            return self.total / self.count

if __name__ == '__main__':
    avg = ThreadSafeAverage()
    avg.add(10)
    avg.add(20)
    print(avg.get_average())