class CommonElementsFinder:
    @staticmethod
    def find_common_elements(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        common_elements = set1.intersection(set2)
        return list(common_elements)

if __name__ == '__main__':
    finder = CommonElementsFinder()
    result1 = finder.find_common_elements([1, 2, 2, 3, 4, 4], [2, 4, 4, 5, 6])
    print(result1)
    result2 = finder.find_common_elements(['apple', 'banana', 'cherry', 'apple', 'date'], ['date', 'fig', 'apple', 'grape'])
    print(result2)
    result3 = finder.find_common_elements([10, 20, 30], [30, 10, 40])
    print(result3)