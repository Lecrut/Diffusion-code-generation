class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.start_index = 0
        self.count = 0

    def push(self, item):
        if self.count < len(self.buffer):
            self.buffer[(self.start_index + self.count) % len(self.buffer)] = item
            self.count += 1
        else:
            self.start_index = (self.start_index + 1) % len(self.buffer)
            self.buffer[(self.start_index + self.count - 1) % len(self.buffer)] = item

    def fetch(self, logical_index):
        if logical_index < 0 or logical_index >= self.count:
            raise IndexError("Index out of bounds")
        physical_index = (self.start_index + logical_index) % len(self.buffer)
        return self.buffer[physical_index]

if __name__ == '__main__':
    cb = CircularBuffer(5)
    for i in range(3):
        cb.push(i * 10)
    print(cb.fetch(0))
    print(cb.fetch(1))
    print(cb.fetch(2))
    for i in range(5, 8):
        cb.push(i * 10)
    print(cb.fetch(0))
    print(cb.fetch(1))
    print(cb.fetch(2))