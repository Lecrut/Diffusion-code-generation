class MiddleElementList:
    def __init__(self, data):
        self._store = list(data)
        self._count = len(self._store)
        self._mid_idx = self._count // 2
        self._cached_mid = self._store[self._mid_idx] if self._count > 0 else None

    def get_middle(self):
        if self._count == 0:
            raise ValueError("Cannot get middle of empty list")
        return self._cached_mid

    def push(self, val):
        self._store.append(val)
        self._count += 1
        new_idx = self._count // 2
        if new_idx != self._mid_idx:
            self._mid_idx = new_idx
            self._cached_mid = self._store[self._mid_idx]

    def remove_last(self):
        if self._count == 0:
            raise ValueError("Cannot remove from empty list")
        self._store.pop()
        self._count -= 1
        new_idx = self._count // 2
        if new_idx != self._mid_idx:
            self._mid_idx = new_idx
            self._cached_mid = self._store[self._mid_idx] if self._count > 0 else None

if __name__ == '__main__':
    nums = [10, 20, 30, 40, 50, 60]
    obj = MiddleElementList(nums)
    print(obj.get_middle())
    obj.push(70)
    print(obj.get_middle())
    obj.remove_last()
    print(obj.get_middle())
    obj.remove_last()
    obj.remove_last()
    obj.remove_last()
    print(obj.get_middle())
    obj.remove_last()
    obj.remove_last()
    obj.remove_last()
    try:
        obj.get_middle()
    except ValueError:
        print("Empty")