class DataComparator:
    def compare(self, list_a, list_b):
        common_elements = 0
        sum_diffs = 0
        min_len = min(len(list_a), len(list_b))
        for i in range(min_len):
            if list_a[i] == list_b[i]:
                common_elements += 1
            else:
                pass
            sum_diffs += abs(list_a[i] - list_b[i])
        return (common_elements, sum_diffs)
if __name__ == '__main__':
    comparator = DataComparator()
    list1 = [1, 5, 3, 8, 2]
    list2 = [1, 6, 3, 9, 2]
    list3 = [10, 20, 30]
    list4 = [10, 20, 30, 40]
    result1 = comparator.compare(list1, list2)
    print(f"Comparing {list1} and {list2}: {result1}")
    result2 = comparator.compare(list1, list3)
    print(f"Comparing {list1} and {list3}: {result2}")
    result3 = comparator.compare(list4, list1)
    print(f"Comparing {list4} and {list1}: {result3}")