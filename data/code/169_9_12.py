class ItemCounter:

    def __init__(self):
        self.small_data = []
        self.large_data = {}

    def add(self, item):
        if len(self.small_data) < 10:
            if item not in self.small_data:
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

    def count(self, item):
        return item in self.small_data or (item in self.large_data and self.large_data[item])
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add('apple')
    counter.add('banana')
    print(counter.count('apple'))
    counter.remove('apple')
    print(counter.count('apple'))
    for _ in range(15):
        counter.add('orange')
    print(counter.count('orange'))
    counter.remove('orange')
    print(counter.count('orange'))
    counter.remove('orange')
    print(counter.count('orange'))
    counter.remove('orange')
    print(counter.count('orange'))