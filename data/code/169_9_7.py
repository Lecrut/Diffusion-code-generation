class ItemCounter:

    def __init__(self):
        self.small = []
        self.large = {}
        self.threshold = 10

    def add(self, item):
        if len(self.small) < self.threshold:
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
    counter.add('apple')
    print(counter.count('apple'))
    counter.remove('apple')
    print(counter.count('apple'))