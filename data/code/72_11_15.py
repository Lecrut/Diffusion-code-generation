class ElementComparator:
    def __init__(self, data):
        self.data = data

    def compare(self, index1, index2):
        return self.data[index1] > self.data[index2]

if __name__ == '__main__':
    comparator = ElementComparator([10, 20, 30, 40, 50])
    print(comparator.compare(0, 5))