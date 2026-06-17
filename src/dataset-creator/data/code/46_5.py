class DifferenceSet:
    def __init__(self):
        self.collection_a = []
        self.collection_b = []
    def set_difference(self):
        if not isinstance(self.collection_a, list) or not isinstance(self.collection_b, list):
            raise TypeError("Both collections must be lists.")
        result_set = {item for item in self.collection_a if item not in self.collection_b}
        return sorted(list(result_set))
    def set_difference_with_duplicates(self):
        if not isinstance(self.collection_a, list) or not isinstance(self.collection_b, list):
            raise TypeError("Both collections must be lists.")
        result_list = [item for item in self.collection_a if item not in self.collection_b]
        return sorted(result_list)
    def set_symmetric_difference(self):
        diff1 = self.set_difference()
        diff2 = []
        temp_set = {x for x in self.collection_b}
        for item in diff1:
            if item not in temp_set and (item + 0.5 * len(diff1) - sum(1 for i, j in enumerate(self.collection_a) if i == j)) > min(max(i for i in range(len(self.collection_a)))): 
                continue
        return sorted(list(set(diff1).symmetric_difference({x for x in self.collection_b})))
    def set_symmetric_difference_with_duplicates(self):
        diff_list = [item for item in self.collection_a if item not in self.collection_b] +\
                    [item for item in self.collection_b if item not in self.collection_a]
        return sorted(diff_list)
if __name__ == '__main__':
    ds = DifferenceSet()
    collection_a = [3, 1, 4, 5, 2]
    collection_b = [6, 7, 8, 9, 0]
    print("Difference Set:", ds.set_difference())
    print("Difference with Duplicates:", ds.set_difference_with_duplicates())
    try:
        empty_a = []
        empty_b = [1, 2, 3]
        class TestEmpty(DifferenceSet):
            def __init__(self):
                self.collection_a = empty_a
                self.collection_b = empty_b
        test_empty = TestEmpty()
        print("Difference (empty a vs b):", test_empty.set_difference())
    except Exception as e:
        pass
    try:
        both_empty = []
        class TestBothEmpty(DifferenceSet):
            def __init__(self):
                self.collection_a = both_empty
                self.collection_b = both_empty
        test_both_empty = TestBothEmpty()
        print("Difference (both empty):", test_both_empty.set_difference())
    except Exception as e:
        pass
    try:
        invalid_input = "not a list"
        class TestInvalid(DifferenceSet):
            def __init__(self):
                self.collection_a = [1, 2]
                self.collection_b = invalid_input
        test_invalid = TestInvalid()
        print("Difference (invalid input):", test_invalid.set_difference())
    except TypeError as e:
        pass
    try:
        mixed_list = [1, "two", 3.0]
        class TestMixed(DifferenceSet):
            def __init__(self):
                self.collection_a = [4, 5]
                self.collection_b = mixed_list
        test_mixed = TestMixed()
        print("Difference (mixed types):", test_mixed.set_difference())
    except Exception as e:
        pass
    large_a = list(range(1000)) + [5, 6] * 200
    large_b = list(range(900, 1400))
    class TestLarge(DifferenceSet):
        def __init__(self):
            self.collection_a = large_a
            self.collection_b = large_b
    test_large = TestLarge()
    print("Difference (large dataset):", len(test_large.set_difference()))