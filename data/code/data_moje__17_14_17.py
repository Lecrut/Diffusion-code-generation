class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.count = 0

    def append(self, value):
        if self.count < self.capacity:
            self.buffer[(self.head + self.count) % self.capacity] = value
            self.count += 1
        else:
            self.buffer[self.head] = value
            self.head = (self.head + 1) % self.capacity

    def get_last_inserted(self):
        if self.count == 0:
            return None
        tail_index = (self.head + self.count - 1) % self.capacity
        return self.buffer[tail_index]

    def get_all(self):
        result = []
        for i in range(self.count):
            index = (self.head + i) % self.capacity
            result.append(self.buffer[index])
        return result

if __name__ == '__main__':
    buf = CircularBuffer(3)
    buf.append(10)
    buf.append(20)
    buf.append(30)
    last_before_overflow = buf.get_last_inserted()
    print(last_before_overflow)
    buf.append(40)
    last_after_overflow = buf.get_last_inserted()
    print(last_after_overflow)
    print(buf.get_all())