class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.count = 0

    def insert(self, item):
        if self.count == self.capacity:
            self.head = (self.head + 1) % self.capacity
        self.buffer[self.head] = item
        if self.count < self.capacity:
            self.count += 1
        next_pos = (self.head + 1) % self.capacity
        return self.buffer[next_pos] if self.count < self.capacity else self.buffer[self.head]

    def get_last_inserted(self):
        if self.count == 0:
            return None
        last_pos = (self.head - 1 + self.capacity) % self.capacity
        return self.buffer[last_pos]

    def get_all(self):
        if self.count == 0:
            return []
        result = []
        for i in range(self.count):
            index = (self.head + i) % self.capacity
            result.append(self.buffer[index])
        return result

if __name__ == '__main__':
    buffer = CircularBuffer(3)
    last_val = buffer.insert(10)
    buffer.insert(20)
    last_val2 = buffer.insert(30)
    buffer.insert(40)
    final_last = buffer.get_last_inserted()
    print(final_last)
    print(buffer.get_all())