class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.start_index = 0

    def append(self, item):
        index = (self.start_index + self.count) % self.size
        self.data[index] = item
        if self.count < self.size:
            self.count += 1
        else:
            self.start_index = (self.start_index + 1) % self.size

    @property
    def count(self):
        return getattr(self, '_count', 0)

    @count.setter
    def count(self, value):
        self._count = value

    def get_element(self, logical_index):
        if logical_index < 0 or logical_index >= self.count:
            raise IndexError("Logical index out of range")
        buffer_index = (self.start_index + logical_index) % self.size
        return self.data[buffer_index]

if __name__ == '__main__':
    buffer = CircularBuffer(5)
    for i in range(7):
        buffer.append(i)
    print(buffer.get_element(0))
    print(buffer.get_element(4))
    print(buffer.get_element(6))