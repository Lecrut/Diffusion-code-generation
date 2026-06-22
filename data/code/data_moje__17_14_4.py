class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.count = 0

    def append(self, item):
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
        else:
            return self.buffer[(self.head - 1) % self.capacity]

    def get_all(self):
        if self.count == 0:
            return []
        result = []
        for i in range(self.count):
            idx = (self.head + i) % self.capacity
            result.append(self.buffer[idx])
        return result

if __name__ == '__main__':
    cb = CircularBuffer(3)
    cb.append(10)
    cb.append(20)
    cb.append(30)
    cb.append(40)

    last_elem = cb.get_last_inserted()
    all_elems = cb.get_all()

    print(last_elem)
    print(all_elems)