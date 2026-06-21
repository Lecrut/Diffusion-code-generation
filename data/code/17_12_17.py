class Deque:
    def __init__(self):
        self.elements = []

    def add_left(self, item):
        self.elements.insert(0, item)

    def add_right(self, item):
        self.elements.append(item)

    def pop_left(self):
        if self.elements:
            return self.elements.pop(0)
        raise IndexError("pop from empty deque")

    def pop_right(self):
        if self.elements:
            return self.elements.pop()
        raise IndexError("pop from empty deque")

    def is_empty(self):
        return len(self.elements) == 0

    def __len__(self):
        return len(self.elements)

def pop_last_added(deque_instance):
    return deque_instance.pop_right()

if __name__ == '__main__':
    d = Deque()
    d.add_right(10)
    d.add_right(20)
    d.add_right(30)
    d.add_right(40)
    d.add_right(50)

    result = pop_last_added(d)
    print(result)