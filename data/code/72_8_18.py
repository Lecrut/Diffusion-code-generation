class ElementComparer:
    @staticmethod
    def compare_elements(list1, list2, index):
        if len(list1) > index and len(list2) > index:
            return list1[index] <= list2[index]
        else:
            raise IndexError("Index out of bounds")

if __name__ == '__main__':
    comparer = ElementComparer()
    result_a = comparer.compare_elements([10, 20, 30], [15, 25, 35], 1)
    print(result_a)
    result_b = comparer.compare_elements([5, 10, 15], [8, 12, 18], 0)
    print(result_b)
    result_c = comparer.compare_elements([100], [99], 0)
    print(result_c)