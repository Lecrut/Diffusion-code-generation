class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def append(self, value):
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity

    def get_last(self):
        if self.size == 0:
            return None
        index = (self.tail - 1) % self.capacity
        return self.buffer[index]

if __name__ == '__main__':
    buffer = CircularBuffer(5)
    buffer.append(10)
    buffer.append(20)
    buffer.append(30)
    buffer.append(40)
    buffer.append(50)
    buffer.append(60)
    buffer.append(70)
    last_value = buffer.get_last()
    print(last_value)