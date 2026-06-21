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
    ic = ItemCounter()
    ic.add('apple')
    ic.add('banana')
    ic.add('apple')
    print(ic.count('apple'))
    ic.remove('apple')
    print(ic.count('apple'))
    ic.add('orange')
    for _ in range(95):
        ic.add('grape')
    print(ic.count('grape'))