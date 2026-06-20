class ElementComparator:
    @staticmethod
    def compare_elements(list1, list2, index):
        val1 = list1[index]
        val2 = list2[index]
        if val1 > val2:
            return "list1 is greater"
        elif val1 < val2:
            return "list2 is greater"
        else:
            return "elements are equal"

if __name__ == '__main__':
    comparator = ElementComparator()
    result = comparator.compare_elements([10, 20, 30, 40], [15, 20, 35, 40], 1)
    print(result)
    result = comparator.compare_elements([5, 10, 15], [5, 12, 15], 1)
    print(result)