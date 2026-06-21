class StringBoundary:
    def __init__(self, items):
        if not items:
            raise ValueError("List must not be empty")
        self.items = items

    def first(self):
        return self.items[0]

    def last(self):
        return self.items[-1]

if __name__ == '__main__':
    data = ["start", "middle", "end"]
    boundary = StringBoundary(data)
    print(boundary.first())
    print(boundary.last())