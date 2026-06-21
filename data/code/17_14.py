class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.size = 0

    def append(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1

    def get_last_inserted(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        return self.buffer[(self.head - 1) % self.capacity]

if __name__ == '__main__':
    buffer = CircularBuffer(3)
    buffer.append(10)
    buffer.append(20)
    buffer.append(30)
    print(buffer.get_last_inserted())
    buffer.append(40)
    print(buffer.get_last_inserted())