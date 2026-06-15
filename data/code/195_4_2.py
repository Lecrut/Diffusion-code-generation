class ListComparator:
    def compare(self, list_a, list_b):
        if len(list_a) != len(list_b):
            return (False, [])
        diff_indices = []
        for i in range(len(list_a)):
            if list_a[i] != list_b[i]:
                diff_indices.append(i)
        return (len(diff_indices) == 0, diff_indices)
if __name__ == '__main__':
    comparator = ListComparator()
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 5]
    list3 = [1, 2, 3, 4]
    list4 = [1, 2, 3, 6]
    list5 = [1, 2, 3]
    result1_2 = comparator.compare(list1, list2)
    print(f"Comparing {list1} and {list2}: {result1_2}")
    result1_3 = comparator.compare(list1, list3)
    print(f"Comparing {list1} and {list3}: {result1_3}")
    result1_4 = comparator.compare(list1, list4)
    print(f"Comparing {list1} and {list4}: {result1_4}")
    result1_5 = comparator.compare(list1, list5)
    print(f"Comparing {list1} and {list5}: {result1_5}")
    result2_3 = comparator.compare(list2, list3)
    print(f"Comparing {list2} and {list3}: {result2_3}")