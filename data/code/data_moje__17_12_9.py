class Deque:
    def __init__(self):
        self.items = []

    def add_last(self, item):
        self.items.append(item)

    def pop_last(self):
        if not self.items:
            raise IndexError("pop from empty deque")
        return self.items.pop()

def create_and_pop():
    d = Deque()
    d.add_last(10)
    d.add_last(20)
    d.add_last(30)
    d.add_last(40)
    d.add_last(50)
    return d.pop_last()

if __name__ == '__main__':
    print(create_and_pop())