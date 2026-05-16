class ListComparator:
    def compare_at_index(self, list1, list2, index):
        val1 = list1[index]
        val2 = list2[index]
        result = {}
        if val1 < val2:
            result = {"list1_element": val1, "list2_element": val2, "operator": "<"}
        elif val1 > val2:
            result = {"list1_element": val1, "list2_element": val2, "operator": ">"}
        else:
            result = {"list1_element": val1, "list2_element": val2, "operator": "="}
        return result
if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [10, 20, 30]
    list_b = [15, 20, 35]
    index_to_compare = 1
    comparison_result = comparator.compare_at_index(list_a, list_b, index_to_compare)
    print(comparison_result)
    list_c = [5, 10, 15]
    list_d = [5, 12, 15]
    index_to_compare_2 = 1
    comparison_result_2 = comparator.compare_at_index(list_c, list_d, index_to_compare_2)
    print(comparison_result_2)
    list_e = [100]
    list_f = [99]
    index_to_compare_3 = 0
    comparison_result_3 = comparator.compare_at_index(list_e, list_f, index_to_compare_3)
    print(comparison_result_3)