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
    for element in [4, 2, 5, 2, 3, 4, 1]:
        counter.add(element)
    print(counter.get_counts())