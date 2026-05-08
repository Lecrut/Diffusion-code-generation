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
    list_b = ['a', 'b', 'c']
    list_c = "not a list"
    list_d = [4, 5]
    result1 = combiner.merge(list_a, list_b)
    print(f"Merge of {list_a} and {list_b}: {result1}")
    result2 = combiner.merge(list_a, list_c)
    print(f"Merge of {list_a} and {list_c}: {result2}")
    result3 = combiner.merge(list_d, list_a)
    print(f"Merge of {list_d} and {list_a}: {result3}")
    result4 = combiner.merge(list_c, list_d)
    print(f"Merge of {list_c} and {list_d}: {result4}")