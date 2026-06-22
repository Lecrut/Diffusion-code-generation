class DirectAccessList:
    def __init__(self):
        self._storage = []

    def append(self, value):
        self._storage.append(value)

    def get(self, index):
        if not 0 <= index < len(self._storage):
            raise IndexError("Index out of bounds")
        return self._storage[index]

if __name__ == '__main__':
    direct_list = DirectAccessList()
    direct_list.append(100)
    direct_list.append(200)
    direct_list.append(300)
    print(direct_list.get(1))