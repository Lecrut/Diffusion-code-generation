class Deque:
    def __init__(self):
        self._items = []

    def append(self, item):
        self._items.append(item)

    def pop_last(self):
        if not self._items:
            raise IndexError("pop from empty deque")
        return self._items.pop()

if __name__ == '__main__':
    dq = Deque()
    dq.append(10)
    dq.append(20)
    dq.append(30)
    dq.append(40)
    result = dq.pop_last()
    print(result)