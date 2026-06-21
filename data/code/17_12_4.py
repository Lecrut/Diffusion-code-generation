class Deque:
    def __init__(self):
        self._data = []

    def push_back(self, value):
        self._data.append(value)

    def pop_back(self):
        return self._data.pop()

if __name__ == '__main__':
    dq = Deque()
    dq.push_back(10)
    dq.push_back(20)
    dq.push_back(30)
    dq.push_back(40)
    dq.push_back(50)
    result = dq.pop_back()
    print(result)