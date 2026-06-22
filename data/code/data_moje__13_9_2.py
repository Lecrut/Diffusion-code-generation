class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start_index = 0
        self.count = 0

    def append(self, item):
        if self.count < self.size:
            self.buffer[(self.start_index + self.count) % self.size] = item
            self.count += 1
        else:
            self.buffer[self.start_index] = item
            self.start_index = (self.start_index + 1) % self.size

    def get(self, logical_index):
        if logical_index < 0 or logical_index >= self.count:
            raise IndexError("Logical index out of range")
        physical_index = (self.start_index + logical_index) % self.size
        return self.buffer[physical_index]

if __name__ == '__main__':
    buffer = CircularBuffer(5)
    for i in range(7):
        buffer.append(i)
    print(buffer.get(0))
    print(buffer.get(6))
    print(buffer.get(3))