class ItemCounter:

    def __init__(self):
        self.small = []
        self.large = {}

    def add(self, item):
        if len(self.small) < 100:
            if item in self.small:
                self.small.remove(item)
            self.small.append(item)
        else:
            if item not in self.large:
                self.large[item] = 0
            self.large[item] += 1

    def remove(self, item):
        if item in self.small:
            self.small.remove(item)
        elif item in self.large:
            self.large[item] -= 1
            if self.large[item] == 0:
                del self.large[item]

    def count(self, item):
        return self.small.count(item) + self.large.get(item, 0)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add('apple')
    counter.add('banana')
    print(counter.count('apple'))
    counter.add('apple')
    print(counter.count('apple'))
    counter.remove('apple')
    print(counter.count('apple'))
    for _ in range(98):
        counter.add('apple')
    print(len(counter.small))
    print(counter.count('apple'))