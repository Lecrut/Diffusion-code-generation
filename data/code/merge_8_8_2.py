class DataComparator:
    def compare_lists(self, list1: list[float], list2: list[float]) -> int:
        sum1 = sum(list1)
        sum2 = sum(list2)
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        else:
            return 0
if __name__ == '__main__':
    data_set_a = [10.5, 20.0, 3.5]
    data_set_b = [5.0, 15.0, 6.5]
    data_set_c = [1.0, 2.0, 3.0]
    comparator = DataComparator()
    result1 = comparator.compare_lists(data_set_a, data_set_b)
    print(f"Comparison between A and B: {result1}")
    result2 = comparator.compare_lists(data_set_a, data_set_c)
    print(f"Comparison between A and C: {result2}")
    result3 = comparator.compare_lists(data_set_b, data_set_b)
    print(f"Comparison between B and B: {result3}")