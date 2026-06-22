class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_last(self):
        if not self._items:
            return None
        return self._items[-1]

if __name__ == '__main__':
    coll = Collection()
    coll.add('first')
    coll.add('second')
    coll.add('third')
    result = coll.get_last()
    print(result)