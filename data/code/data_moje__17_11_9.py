class OrderedCollection:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_last(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

if __name__ == '__main__':
    collection = OrderedCollection()
    collection.add("first")
    collection.add("second")
    collection.add("third")
    result = collection.get_last()
    print(result)