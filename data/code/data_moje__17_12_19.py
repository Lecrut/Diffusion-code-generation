class Deque:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def pop_last(self):
        if not self.items:
            return None
        return self.items.pop()

def main():
    d = Deque()
    d.add(10)
    d.add(20)
    d.add(30)
    d.add(40)
    d.add(50)
    result = d.pop_last()
    print(result)

if __name__ == '__main__':
    main()