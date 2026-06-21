class Deque:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def pop_last(self):
        if not self.items:
            raise IndexError("pop from empty deque")
        return self.items.pop()

if __name__ == '__main__':
    deque = Deque()
    deque.append(10)
    deque.append(20)
    deque.append(30)
    deque.append(40)
    result = deque.pop_last()
    print(result)