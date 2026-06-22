class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start_index = 0
        self.end_index = 0
        self.size = 0

    def push(self, value):
        if self.size == self.capacity:
            self.start_index = (self.start_index + 1) % self.capacity
            self.size -= 1
        self.buffer[self.end_index] = value
        self.end_index = (self.end_index + 1) % self.capacity
        self.size += 1

    def get_last(self):
        if self.size == 0:
            return None
        last_index = (self.end_index - 1 + self.capacity) % self.capacity
        return self.buffer[last_index]

if __name__ == '__main__':
    cb = CircularBuffer(5)
    cb.push(10)
    cb.push(20)
    cb.push(30)
    cb.push(40)
    cb.push(50)
    cb.push(60)
    cb.push(70)
    result = cb.get_last()
    print(result)