class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if index < 0 or index >= len(list1) or index >= len(list2):
            return {"error": "Index out of bounds"}
        val1 = list1[index]
        val2 = list2[index]
        if val1 < val2:
            return {"list1_element": val1, "list2_element": val2, "operator": "<"}
        elif val1 > val2:
            return {"list1_element": val1, "list2_element": val2, "operator": ">"}
        else:
            return {"list1_element": val1, "list2_element": val2, "operator": "="}
if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [10, 20, 30, 40]
    list_b = [10, 25, 30, 45]
    index_to_compare = 1
    result1 = comparator.compare_at_index(list_a, list_b, index_to_compare)
    print(f"Comparing {list_a} and {list_b} at index {index_to_compare}: {result1}")
    list_c = [5, 15, 25]
    list_d = [5, 10, 30]
    index_to_compare_2 = 1
    result2 = comparator.compare_at_index(list_c, list_d, index_to_compare_2)
    print(f"Comparing {list_c} and {list_d} at index {index_to_compare_2}: {result2}")
    list_e = [1, 2, 3]
    list_f = [1, 2, 3]
    index_to_compare_3 = 0
    result3 = comparator.compare_at_index(list_e, list_f, index_to_compare_3)
    print(f"Comparing {list_e} and {list_f} at index {index_to_compare_3}: {result3}")
    list_g = [100]
    list_h = [100, 200]
    index_to_compare_4 = 0
    result4 = comparator.compare_at_index(list_g, list_h, index_to_compare_4)
    print(f"Comparing {list_g} and {list_h} at index {index_to_compare_4}: {result4}")