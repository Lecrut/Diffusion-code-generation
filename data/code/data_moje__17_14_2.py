class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.count = 0

    def insert(self, value):
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.capacity
        if self.count < self.capacity:
            self.count += 1

    def get_last_inserted(self):
        if self.count == 0:
            return None
        return self.buffer[(self.head - 1) % self.capacity]

    def get_all(self):
        result = []
        if self.count == 0:
            return result
        start_index = (self.head - self.count) % self.capacity
        for i in range(self.count):
            index = (start_index + i) % self.capacity
            result.append(self.buffer[index])
        return result

if __name__ == '__main__':
    buffer = CircularBuffer(5)
    buffer.insert(10)
    buffer.insert(20)
    buffer.insert(30)
    last_val = buffer.get_last_inserted()
    print(last_val)
    buffer.insert(40)
    buffer.insert(50)
    buffer.insert(60)
    last_val_after = buffer.get_last_inserted()
    print(last_val_after)
    all_vals = buffer.get_all()
    print(all_vals)