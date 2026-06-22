class Deque:
    def __init__(self):
        self._data = []

    def append(self, item):
        self._data.append(item)

    def pop_last(self):
        return self._data.pop()

if __name__ == '__main__':
    dq = Deque()
    dq.append(10)
    dq.append(20)
    dq.append(30)
    dq.append(40)
    result = dq.pop_last()
    print(result)