class CollectionComparator:
    def compare_collections(self, list1, list2):
        sorted_list1 = sorted(list1)
        sorted_list2 = sorted(list2)
        if len(sorted_list1) != len(sorted_list2):
            return "Lengths are different"
        comparison_result = []
        for i in range(len(sorted_list1)):
            diff = sorted_list1[i] - sorted_list2[i]
            comparison_result.append(diff)
        if all(d == 0 for d in comparison_result):
            return "Collections are identical"
        else:
            return comparison_result
if __name__ == '__main__':
    comparator = CollectionComparator()
    data1 = [5, 2, 8, 1]
    data2 = [1, 2, 5, 8]
    result = comparator.compare_collections(data1, data2)
    print(result)