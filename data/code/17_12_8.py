class Deque:
    def __init__(self):
        self._items = []

    def append(self, value):
        self._items.append(value)

    def pop_last(self):
        return self._items.pop()

if __name__ == '__main__':
    dq = Deque()
    dq.append(10)
    dq.append(20)
    dq.append(30)
    dq.append(40)
    result = dq.pop_last()
    print(result)