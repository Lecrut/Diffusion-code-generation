class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def insert(self, value):
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.capacity
        if self.count < self.capacity:
            self.count += 1
        else:
            self.tail = (self.tail + 1) % self.capacity

    def get_last_inserted(self):
        if self.count == 0:
            return None
        prev_head = (self.head - 1) % self.capacity
        return self.buffer[prev_head]

if __name__ == '__main__':
    cb = CircularBuffer(3)
    cb.insert(10)
    cb.insert(20)
    cb.insert(30)
    cb.insert(40)
    last_val = cb.get_last_inserted()
    print(last_val)