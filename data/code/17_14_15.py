class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, value):
        if self.count == self.capacity:
            self.head = (self.head + 1) % self.capacity
            self.count = self.capacity
        else:
            self.count += 1
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity

    def get_last_inserted(self):
        if self.count == 0:
            raise IndexError("Buffer is empty")
        if self.count < self.capacity:
            return self.buffer[(self.tail - 1 + self.capacity) % self.capacity]
        return self.buffer[(self.tail - 1 + self.capacity) % self.capacity]

if __name__ == '__main__':
    cb = CircularBuffer(3)
    cb.push(10)
    cb.push(20)
    cb.push(30)
    print(cb.get_last_inserted())
    cb.push(40)
    print(cb.get_last_inserted())
    cb.push(50)
    print(cb.get_last_inserted())