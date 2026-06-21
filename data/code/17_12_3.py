class Deque:
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.append(item)

    def pop_rear(self):
        if self.is_empty():
            raise IndexError("pop from empty deque")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def main():
    d = Deque()
    d.add_rear(10)
    d.add_rear(20)
    d.add_rear(30)
    d.add_rear(40)
    d.add_rear(50)
    result = d.pop_rear()
    print(result)

if __name__ == '__main__':
    main()