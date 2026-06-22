class ElementComparator:
    def __init__(self, data):
        self.data = data

    def compare(self):
        return self.data[0] > self.data[5]

if __name__ == '__main__':
    sample = [10, 2, 3, 4, 5, 1]
    comparator = ElementComparator(sample)
    print(comparator.compare())