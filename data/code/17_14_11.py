class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * capacity
        self._head = 0
        self._count = 0

    def push(self, value):
        index = (self._head + self._count) % self._capacity
        self._data[index] = value
        if self._count < self._capacity:
            self._count += 1
        else:
            self._head = (self._head + 1) % self._capacity

    def get_last_inserted(self):
        if self._count == 0:
            return None
        last_index = (self._head + self._count - 1) % self._capacity
        return self._data[last_index]

    def is_full(self):
        return self._count == self._capacity

    def is_empty(self):
        return self._count == 0

if __name__ == '__main__':
    buffer = CircularBuffer(3)
    buffer.push(10)
    buffer.push(20)
    buffer.push(30)
    last_val = buffer.get_last_inserted()
    print(last_val)
    buffer.push(40)
    last_val_new = buffer.get_last_inserted()
    print(last_val_new)