class CollectionComparator:
    def compare_collections(self, collection1, collection2):
        sorted_list1 = sorted(collection1)
        sorted_list2 = sorted(collection2)
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
    data1 = [1, 5, 3, 8]
    data2 = [3, 1, 5, 8]
    result = comparator.compare_collections(data1, data2)
    print(result)
    data3 = [10, 20, 30]
    data4 = [10, 25, 30]
    result2 = comparator.compare_collections(data3, data4)
    print(result2)
    data5 = [1, 2, 3]
    data6 = [1, 2, 4]
    result3 = comparator.compare_collections(data5, data6)
    print(result3)