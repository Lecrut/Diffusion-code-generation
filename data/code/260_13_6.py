class CollectionComparator:
    def compare_collections(self, list1, list2):
        list1.sort()
        list2.sort()
        comparison_result = []
        len1 = len(list1)
        len2 = len(list2)
        min_len = min(len1, len2)
        for i in range(min_len):
            if list1[i] < list2[i]:
                comparison_result.append("list1 is smaller at index")
            elif list1[i] > list2[i]:
                comparison_result.append("list2 is smaller at index")
            else:
                comparison_result.append(f"Equal at index {i}")
        if len1 != len2:
            if len1 > len2:
                comparison_result.append(f"list1 has {len1 - len2} extra elements")
            else:
                comparison_result.append(f"list2 has {len2 - len1} extra elements")
        return comparison_result
if __name__ == '__main__':
    comparator = CollectionComparator()
    data1 = [5, 2, 8, 1]
    data2 = [1, 3, 7, 9]
    results = comparator.compare_collections(data1, data2)
    for result in results:
        print(result)