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
    collection = Collection()
    collection.add("First")
    collection.add("Second")
    collection.add("Third")
    result = collection.get_last()
    print(result)