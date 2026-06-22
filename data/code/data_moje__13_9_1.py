class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.start_index = 0

    def append(self, item):
        index = self.start_index
        self.buffer[index] = item
        self.start_index = (self.start_index + 1) % self.size

    def get(self, logical_index):
        if self.size == 0:
            return None
        if logical_index < 0:
            logical_index = self.size + (logical_index % self.size)
        actual_index = (self.start_index + logical_index) % self.size
        if self.buffer[actual_index] is None:
            return None
        return self.buffer[actual_index]

if __name__ == '__main__':
    cb = CircularBuffer(5)
    cb.append('A')
    cb.append('B')
    cb.append('C')
    cb.append('D')
    cb.append('E')
    cb.append('F')
    result1 = cb.get(0)
    result2 = cb.get(4)
    result3 = cb.get(5)
    result4 = cb.get(-1)
    print(result1)
    print(result2)
    print(result3)
    print(result4)