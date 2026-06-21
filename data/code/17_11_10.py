class Collection:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_last(self):
        if not self.items:
            return None
        return self.items[-1]

if __name__ == '__main__':
    c = Collection()
    c.add("apple")
    c.add("banana")
    c.add("cherry")
    print(c.get_last())