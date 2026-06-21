class Deque:
    def __init__(self):
        self.items = []

    def push_back(self, value):
        self.items.append(value)

    def pop_back(self):
        return self.items.pop()

def main():
    dq = Deque()
    for val in [10, 20, 30, 40, 50]:
        dq.push_back(val)
    result = dq.pop_back()
    print(result)

if __name__ == '__main__':
    main()