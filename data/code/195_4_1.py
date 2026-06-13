class ListComparator:
    def compare(self, list_a, list_b):
        if len(list_a) != len(list_b):
            return (False, [])
        differing_indices = []
        for i in range(len(list_a)):
            if list_a[i] != list_b[i]:
                differing_indices.append(i)
        return (len(differing_indices) == 0, differing_indices)
if __name__ == '__main__':
    comparator = ListComparator()
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 5, 4]
    list3 = [1, 2, 3, 4]
    list4 = [1, 2, 3, 5]
    list5 = [1, 2, 3]
    result1 = comparator.compare(list1, list3)
    print(f"Comparing {list1} and {list3}: {result1}")
    result2 = comparator.compare(list1, list2)
    print(f"Comparing {list1} and {list2}: {result2}")
    result3 = comparator.compare(list1, list4)
    print(f"Comparing {list1} and {list4}: {result3}")
    result4 = comparator.compare(list1, list5)
    print(f"Comparing {list1} and {list5}: {result4}")
    result5 = comparator.compare(list2, list1)
    print(f"Comparing {list2} and {list1}: {result5}")