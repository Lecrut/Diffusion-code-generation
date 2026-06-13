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
    list2 = [1, 5, 3, 4]
    list3 = [1, 2, 3, 4]
    list4 = [1, 2, 3, 5]
    list5 = [1, 2, 3]
    list6 = [1, 2, 3, 4, 5]
    result1 = comparator.compare(list1, list3)
    print(f"Comparing {list1} and {list3}: Equality={result1[0]}, Indices={result1[1]}")
    result2 = comparator.compare(list1, list2)
    print(f"Comparing {list1} and {list2}: Equality={result2[0]}, Indices={result2[1]}")
    result3 = comparator.compare(list1, list4)
    print(f"Comparing {list1} and {list4}: Equality={result3[0]}, Indices={result3[1]}")
    result4 = comparator.compare(list1, list5)
    print(f"Comparing {list1} and {list5}: Equality={result4[0]}, Indices={result4[1]}")
    result5 = comparator.compare(list6, list1)
    print(f"Comparing {list6} and {list1}: Equality={result5[0]}, Indices={result5[1]}")