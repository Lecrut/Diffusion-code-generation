class ListCombiner:
    def merge(self, list1, list2):
        try:
            if not isinstance(list1, list) or not isinstance(list2, list):
                raise TypeError("Both inputs must be lists.")
            return list1 + list2
        except TypeError as e:
            return [f"Error: {e}"]
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
    result3 = combiner.merge(list_d, [9, 10])
    print(f"Merge of {list_d} and [9, 10]: {result3}")
    result4 = combiner.merge(10, list_b)
    print(f"Merge of 10 and {list_b}: {result4}")