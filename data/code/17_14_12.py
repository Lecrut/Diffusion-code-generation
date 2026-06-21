class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start = 0
        self.count = 0

    def add(self, value):
        index = (self.start + self.count) % self.capacity
        self.buffer[index] = value
        if self.count < self.capacity:
            self.count += 1
        else:
            self.start = (self.start + 1) % self.capacity

    def get_last_inserted(self):
        if self.count == 0:
            return None
        index = (self.start + self.count - 1) % self.capacity
        return self.buffer[index]

    def get_all(self):
        if self.count == 0:
            return []
        result = []
        for i in range(self.count):
            index = (self.start + i) % self.capacity
            result.append(self.buffer[index])
        return result

if __name__ == '__main__':
    buffer = CircularBuffer(5)
    values = [10, 20, 30, 40, 50, 60, 70]
    for val in values:
        buffer.add(val)
    last_val = buffer.get_last_inserted()
    all_vals = buffer.get_all()
    print(last_val)
    print(all_vals)