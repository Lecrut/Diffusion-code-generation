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
    d = Deque()
    d.append(10)
    d.append(20)
    d.append(30)
    d.append(40)
    print(d.pop_last())
    print(d.pop_last())
    print(d.pop_last())