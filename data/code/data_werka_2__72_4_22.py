class IndexElementExtractor:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def extract(self, index):
        if index < 0 or index >= len(self.list_a) or index >= len(self.list_b):
            raise ValueError("Index out of range")
        return [(self.list_a[index], self.list_b[index])]

if __name__ == '__main__':
    extractor = IndexElementExtractor([10, 20, 30], ['a', 'b', 'c'])
    result = extractor.extract(0)
    print(result)
    result2 = extractor.extract(2)
    print(result2)