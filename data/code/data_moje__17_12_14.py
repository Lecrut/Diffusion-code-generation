class Deque:
    def __init__(self):
        self.items = []

    def append(self, value):
        self.items.append(value)

    def pop_back(self):
        return self.items.pop()

if __name__ == '__main__':
    dq = Deque()
    dq.append(10)
    dq.append(20)
    dq.append(30)
    result = dq.pop_back()
    print(result)