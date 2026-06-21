class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity
        else:
            tail = (self.head + self.size) % self.capacity
            self.buffer[tail] = item
            self.size += 1

    def get(self, logical_index):
        if logical_index < 0 or logical_index >= self.size:
            return None
        effective_index = (self.head + logical_index) % self.capacity
        return self.buffer[effective_index]

if __name__ == '__main__':
    cb = CircularBuffer(3)
    cb.append(10)
    cb.append(20)
    cb.append(30)
    val = cb.get(1)
    print(val)