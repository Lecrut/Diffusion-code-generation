class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.count = 0

    def push(self, item):
        if self.count < self.capacity:
            self.buffer[(self.head + self.count) % self.capacity] = item
            self.count += 1
        else:
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity

    def get_last_inserted(self):
        if self.count == 0:
            return None
        if self.count < self.capacity:
            return self.buffer[(self.head + self.count - 1) % self.capacity]
        return self.buffer[(self.head - 1) % self.capacity]

if __name__ == '__main__':
    buf = CircularBuffer(3)
    buf.push(10)
    buf.push(20)
    buf.push(30)
    print(buf.get_last_inserted())
    buf.push(40)
    print(buf.get_last_inserted())
    buf.push(50)
    print(buf.get_last_inserted())