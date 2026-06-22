class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0

    def append(self, value):
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1

    def get_last_inserted(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        index = (self.head - 1) % self.capacity
        return self.buffer[index]

    def get_all(self):
        if self.size == 0:
            return []
        if self.head > self.size:
            return self.buffer[self.head - self.size:self.head] + self.buffer[:self.head % self.size]
        return self.buffer[:self.size]

if __name__ == '__main__':
    buffer = CircularBuffer(5)
    values = [10, 20, 30, 40, 50, 60, 70]
    for val in values:
        buffer.append(val)
    last_val = buffer.get_last_inserted()
    print(last_val)
    all_vals = buffer.get_all()
    print(all_vals)