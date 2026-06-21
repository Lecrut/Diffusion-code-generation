class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def push(self, value):
        if self.size == self.capacity:
            self.buffer[self.end] = value
            self.end = (self.end + 1) % self.capacity
            self.start = (self.start + 1) % self.capacity
        else:
            self.buffer[self.end] = value
            self.end = (self.end + 1) % self.capacity
            self.size += 1

    def get_last_inserted(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        index = (self.end - 1) % self.capacity
        return self.buffer[index]

if __name__ == '__main__':
    buffer = CircularBuffer(3)
    buffer.push(10)
    buffer.push(20)
    buffer.push(30)
    buffer.push(40)
    buffer.push(50)
    print(buffer.get_last_inserted())