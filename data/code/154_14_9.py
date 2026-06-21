class ElementCounter:
    def __init__(self):
        self.counts = {}

    def add(self, item):
        if item in self.counts:
            self.counts[item] += 1
        else:
            self.counts[item] = 1

    def get_counts(self):
        return dict(sorted(self.counts.items()))

if __name__ == '__main__':
    counter = ElementCounter()
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    for item in items:
        counter.add(item)
    print(counter.get_counts())