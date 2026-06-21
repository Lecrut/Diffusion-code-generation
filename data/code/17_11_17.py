class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_last_entry(self):
        if not self._items:
            return None
        return self._items[-1]

if __name__ == '__main__':
    coll = Collection()
    coll.add(10)
    coll.add(20)
    coll.add(30)
    print(coll.get_last_entry())
    coll.add(40)
    print(coll.get_last_entry())