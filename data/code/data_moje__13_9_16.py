class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start = 0
        self.size = 0

    def append(self, value):
        end_index = (self.start + self.size) % self.capacity
        self.buffer[end_index] = value
        if self.size < self.capacity:
            self.size += 1
        else:
            self.start = (self.start + 1) % self.capacity

    def get(self, logical_index):
        if logical_index < 0 or logical_index >= self.size:
            raise IndexError("Logical index out of range")
        actual_index = (self.start + logical_index) % self.capacity
        return self.buffer[actual_index]

def fetch_element(logical_index, start, size, capacity, buffer):
    if logical_index < 0 or logical_index >= size:
        raise IndexError("Logical index out of range")
    actual_index = (start + logical_index) % capacity
    return buffer[actual_index]

if __name__ == '__main__':
    buffer = CircularBuffer(5)
    for val in [10, 20, 30, 40, 50]:
        buffer.append(val)
    
    buffer.append(60)
    buffer.append(70)
    
    val = buffer.get(2)
    print(val)
    
    func_val = fetch_element(1, 3, 5, 5, [10, 20, 30, 40, 50])
    print(func_val)