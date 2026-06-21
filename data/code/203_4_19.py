class ElementwiseComparator:
    def count_greater_positions(self, list1, list2):
        return sum(1 for i in range(len(list1)) if list1[i] > list2[i])

if __name__ == '__main__':
    comparator = ElementwiseComparator()
    result1 = comparator.count_greater_positions([1, 3, 5], [0, 2, 4])
    print(f"Count of positions where first list's elements are greater: {result1}")
    
    result2 = comparator.count_greater_positions([-2, -1, 0], [-3, -2, -1])
    print(f"Count of positions where first list's elements are greater: {result2}")