class CircularBuffer:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._buffer = [None] * capacity
        self._head = 0
        self._count = 0
        self._is_full = False

    def push(self, item):
        index = (self._head + self._count) % self._capacity
        if self._is_full:
            self._buffer[self._head] = item
            self._head = (self._head + 1) % self._capacity
        else:
            self._buffer[index] = item
            self._count += 1
            if self._count == self._capacity:
                self._is_full = True

    def get_last_inserted(self):
        if self._count == 0:
            raise IndexError("Buffer is empty")
        if self._is_full:
            return self._buffer[self._head]
        return self._buffer[(self._head + self._count - 1) % self._capacity]

    def get_all_elements(self):
        if self._count == 0:
            return []
        result = []
        for i in range(self._count):
            index = (self._head + i) % self._capacity
            result.append(self._buffer[index])
        return result

    @property
    def count(self):
        return self._count

    @property
    def capacity(self):
        return self._capacity

if __name__ == '__main__':
    buffer = CircularBuffer(3)
    buffer.push(10)
    buffer.push(20)
    buffer.push(30)
    last = buffer.get_last_inserted()
    print(last)
    buffer.push(40)
    last_after_push = buffer.get_last_inserted()
    print(last_after_push)
    all_elements = buffer.get_all_elements()
    print(all_elements)