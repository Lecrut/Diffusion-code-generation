class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.write_index = 0
        self.count = 0

    def insert(self, value):
        self.buffer[self.write_index] = value
        self.write_index = (self.write_index + 1) % self.capacity
        if self.count < self.capacity:
            self.count += 1

    def get_last_inserted(self):
        if self.count == 0:
            raise IndexError("Buffer is empty")
        if self.count == self.capacity:
            return self.buffer[(self.write_index - 1) % self.capacity]
        return self.buffer[(self.write_index - 1) % self.capacity]

if __name__ == '__main__':
    sample_buffer = CircularBuffer(5)
    initial_values = [10, 20, 30, 40, 50, 60, 70]
    for value in initial_values:
        sample_buffer.insert(value)
    print(sample_buffer.get_last_inserted())