class CollectionComparator:
    def compare_collections(self, list1, list2):
        if len(list1) != len(list2):
            return "Lengths are different"
        sorted_list1 = sorted(list1)
        sorted_list2 = sorted(list2)
        for i in range(len(sorted_list1)):
            if sorted_list1[i] != sorted_list2[i]:
                return f"Mismatch found at index {i}: {sorted_list1[i]} vs {sorted_list2[i]}"
        return "Collections are identical"
if __name__ == '__main__':
    comparator = CollectionComparator()
    data1 = [5, 1, 8, 3]
    data2 = [3, 5, 1, 8]
    data3 = [1, 2, 3, 4]
    data4 = [1, 2, 5, 6]
    result1 = comparator.compare_collections(data1, data2)
    print(f"Comparing {data1} and {data2}: {result1}")
    result2 = comparator.compare_collections(data3, data4)
    print(f"Comparing {data3} and {data4}: {result2}")
    data5 = [10, 20, 30]
    data6 = [10, 20, 31]
    result3 = comparator.compare_collections(data5, data6)
    print(f"Comparing {data5} and {data6}: {result3}")
    data7 = [1, 5, 9]
    data8 = [1, 5, 10]
    result4 = comparator.compare_collections(data7, data8)
    print(f"Comparing {data7} and {data8}: {result4}")