class ItemCounter:

    def __init__(self):
        self.small_data = []
        self.large_data = {}

    def add(self, item):
        if len(self.small_data) < 100:
            if item in self.small_data:
                self.small_data.remove(item)
            self.small_data.append(item)
        else:
            if item not in self.large_data:
                self.large_data[item] = 0
            self.large_data[item] += 1

    def remove(self, item):
        if item in self.small_data:
            self.small_data.remove(item)
        elif item in self.large_data:
            self.large_data[item] -= 1
            if self.large_data[item] == 0:
                del self.large_data[item]

    def query(self, item):
        if item in self.small_data:
            return len(self.small_data) - self.small_data.index(item)
        elif item in self.large_data:
            return self.large_data[item]
        return 0
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add('apple')
    counter.add('banana')
    print(counter.query('apple'))
    counter.remove('apple')
    print(counter.query('apple'))
    for _ in range(98):
        counter.add('apple')
    print(counter.query('apple'))