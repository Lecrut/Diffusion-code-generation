class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.count = 0

    def insert(self, value):
        if self.count == self.capacity:
            self.buffer[self.head] = value
            self.head = (self.head + 1) % self.capacity
        else:
            idx = (self.head + self.count) % self.capacity
            self.buffer[idx] = value
            self.count += 1

    def get_last(self):
        if self.count == 0:
            return None
        last_idx = (self.head + self.count - 1) % self.capacity
        return self.buffer[last_idx]

def main():
    buf = CircularBuffer(3)
    buf.insert(10)
    buf.insert(20)
    buf.insert(30)
    result = buf.get_last()
    print(result)
    buf.insert(40)
    result2 = buf.get_last()
    print(result2)

if __name__ == '__main__':
    main()