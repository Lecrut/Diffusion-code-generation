class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, value):
        if self.count == self.capacity:
            self.buffer[self.tail] = value
            self.tail = (self.tail + 1) % self.capacity
            self.head = (self.head + 1) % self.capacity
        else:
            self.buffer[self.head] = value
            self.head = (self.head + 1) % self.capacity
            self.count += 1

    def get_last_inserted(self):
        if self.count == 0:
            return None
        if self.count < self.capacity:
            index = (self.head - 1) % self.capacity
        else:
            index = self.tail
        return self.buffer[index]

if __name__ == '__main__':
    buffer = CircularBuffer(3)
    buffer.push(10)
    buffer.push(20)
    buffer.push(30)
    buffer.push(40)
    result = buffer.get_last_inserted()
    print(result)