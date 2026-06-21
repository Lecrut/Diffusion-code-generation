class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.count = 0

    def push(self, value):
        if self.count == self.capacity:
            self.buffer[self.head] = value
            self.head = (self.head + 1) % self.capacity
        else:
            index = (self.head + self.count) % self.capacity
            self.buffer[index] = value
            self.count += 1

    def get_last_inserted(self):
        if self.count == 0:
            return None
        if self.count < self.capacity:
            index = (self.head + self.count - 1) % self.capacity
        else:
            index = (self.head - 1) % self.capacity
        return self.buffer[index]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

if __name__ == '__main__':
    buffer_obj = CircularBuffer(3)
    buffer_obj.push(10)
    buffer_obj.push(20)
    buffer_obj.push(30)
    result = buffer_obj.get_last_inserted()
    print(result)
    buffer_obj.push(40)
    result = buffer_obj.get_last_inserted()
    print(result)