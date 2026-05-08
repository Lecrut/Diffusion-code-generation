class ListCombiner:
    def merge(self, list1, list2):
        try:
            combined_list = list1 + list2
            return combined_list
        except TypeError:
            return "Error: One or both inputs are not list-like."
if __name__ == '__main__':
    combiner = ListCombiner()
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    list_c = "not a list"
    list_d = [7, 8]
    result1 = combiner.merge(list_a, list_b)
    print(f"Merge of {list_a} and {list_b}: {result1}")
    result2 = combiner.merge(list_a, list_c)
    print(f"Merge of {list_a} and {list_c}: {result2}")
    result3 = combiner.merge(list_d, list_a)
    print(f"Merge of {list_d} and {list_a}: {result3}")