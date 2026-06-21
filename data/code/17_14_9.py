class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.size = 0

    def push(self, item):
        if self.size < self.capacity:
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity
            self.size += 1
        else:
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity

    def get_last_inserted(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        if self.size < self.capacity:
            idx = (self.head - 1 + self.capacity) % self.capacity
        else:
            idx = (self.head - 1 + self.capacity) % self.capacity
        return self.buffer[idx]

    def get_all(self):
        result = []
        for i in range(self.size):
            idx = (self.head - self.size + i + self.capacity) % self.capacity
            result.append(self.buffer[idx])
        return result

if __name__ == '__main__':
    cb = CircularBuffer(3)
    cb.push(10)
    cb.push(20)
    cb.push(30)
    last = cb.get_last_inserted()
    print(last)
    cb.push(40)
    last_after_overwrite = cb.get_last_inserted()
    print(last_after_overwrite)
    print(cb.get_all())