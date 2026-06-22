class Deque:
    def __init__(self):
        self._data = []

    def append(self, value):
        self._data.append(value)

    def pop_back(self):
        return self._data.pop()

if __name__ == '__main__':
    dq = Deque()
    dq.append(10)
    dq.append(20)
    dq.append(30)
    result = dq.pop_back()
    print(result)