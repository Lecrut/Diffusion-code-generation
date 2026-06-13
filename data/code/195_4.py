class ListComparator:
    def compare(self, list_a, list_b):
        if len(list_a) != len(list_b):
            return (False, [])
        differing_indices = []
        for i in range(len(list_a)):
            if list_a[i] != list_b[i]:
                differing_indices.append(i)
        return (list_a == list_b, differing_indices)
if __name__ == '__main__':
    comparator = ListComparator()
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 5, 4]
    list3 = [1, 2, 3, 4]
    list4 = [1, 2, 3]
    result1 = comparator.compare(list1, list2)
    print(f"Comparing {list1} and {list2}: Equality={result1[0]}, Differing Indices={result1[1]}")
    result2 = comparator.compare(list1, list3)
    print(f"Comparing {list1} and {list3}: Equality={result2[0]}, Differing Indices={result2[1]}")
    result3 = comparator.compare(list1, list4)
    print(f"Comparing {list1} and {list4}: Equality={result3[0]}, Differing Indices={result3[1]}")
    list5 = [1, 2, 3, 4]
    list6 = [1, 2, 3, 4]
    result4 = comparator.compare(list5, list6)
    print(f"Comparing {list5} and {list6}: Equality={result4[0]}, Differing Indices={result4[1]}")
    list7 = [1, 2, 3]
    list8 = [1, 2, 3, 4]
    result5 = comparator.compare(list7, list8)
    print(f"Comparing {list7} and {list8}: Equality={result5[0]}, Differing Indices={result5[1]}")