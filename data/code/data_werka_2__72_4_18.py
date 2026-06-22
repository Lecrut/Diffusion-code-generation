class IndexExtractor:
    def __init__(self, list_one, list_two):
        self.list_one = list_one
        self.list_two = list_two

    def extract_pair(self, index):
        if index < 0 or index >= len(self.list_one) or index >= len(self.list_two):
            raise ValueError("Index out of range for one or both lists")
        return [(self.list_one[index], self.list_two[index])]

if __name__ == '__main__':
    extractor = IndexExtractor([10, 20, 30], [40, 50, 60])
    print(extractor.extract_pair(1))
    print(extractor.extract_pair(0))