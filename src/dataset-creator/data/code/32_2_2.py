class SetCounter:
    def __init__(self, data):
        self._data = data
        self._count = 0
    def count(self):
        self._count = len(self._data)
        return self._count
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    counter = SetCounter(sample_list)
    total = counter.count()
    print(total)