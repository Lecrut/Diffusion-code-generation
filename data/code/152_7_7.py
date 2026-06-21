class CommonElementsExtractor:
    @staticmethod
    def extract(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        common_elements = set1.intersection(set2)
        return list(common_elements)

if __name__ == '__main__':
    extractor = CommonElementsExtractor()
    result1 = extractor.extract([1, 2, 2, 3, 4, 4], [2, 4, 4, 5, 6])
    print(result1)
    result2 = extractor.extract(['apple', 'banana', 'cherry', 'apple'], ['date', 'fig', 'apple', 'grape'])
    print(result2)
    result3 = extractor.extract([10, 20, 30], [30, 10, 40])
    print(result3)