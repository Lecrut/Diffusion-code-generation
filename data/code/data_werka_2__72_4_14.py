class IndexElementExtractor:
    def __init__(self, first_list, second_list):
        self.first_list = first_list
        self.second_list = second_list

    def extract(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.first_list) or index < 0 or index >= len(self.second_list):
            raise ValueError("Index out of range")
        return [(self.first_list[index], self.second_list[index])]

    def extract_all(self):
        results = []
        length = min(len(self.first_list), len(self.second_list))
        for i in range(length):
            results.append([(self.first_list[i], self.second_list[i])])
        return results

if __name__ == '__main__':
    extractor = IndexElementExtractor([10, 20, 30], [40, 50, 60])
    print(extractor.extract(1))
    print(extractor.extract_all())