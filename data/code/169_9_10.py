class ItemCounter:

    def __init__(self):
        self._small = []
        self._large = {}
        self._threshold = 10

    def add(self, item):
        if len(self._small) < self._threshold:
            if item not in self._small:
                self._small.append(item)
        else:
            if item not in self._large:
                self._large[item] = 0
            self._large[item] += 1

    def remove(self, item):
        if item in self._small:
            self._small.remove(item)
        elif item in self._large:
            self._large[item] -= 1
            if self._large[item] == 0:
                del self._large[item]

    def count(self, item):
        return self._small.count(item) + self._large.get(item, 0)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add('apple')
    counter.add('banana')
    counter.add('apple')
    print(counter.count('apple'))
    counter.remove('apple')
    print(counter.count('apple'))