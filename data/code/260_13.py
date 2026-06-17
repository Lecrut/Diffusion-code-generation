class CollectionComparer:
    def compare_collections(self, list1, list2):
        sorted_list1 = sorted(list1)
        sorted_list2 = sorted(list2)
        if len(sorted_list1) != len(sorted_list2):
            return "Lengths are different"
        comparison_result = []
        for i in range(len(sorted_list1)):
            diff = sorted_list1[i] - sorted_list2[i]
            comparison_result.append(f"Index {i}: List1={sorted_list1[i]}, List2={sorted_list2[i]}, Difference={diff}")
        return comparison_result
if __name__ == '__main__':
    comparer = CollectionComparer()
    data1 = [5, 1, 8, 3]
    data2 = [1, 3, 5, 8]
    result = comparer.compare_collections(data1, data2)
    for line in result:
        print(line)