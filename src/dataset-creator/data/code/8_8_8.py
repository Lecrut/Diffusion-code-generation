class DataComparer:
    def compare_collections(self, list1: list[float], list2: list[float]) -> int:
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
    data_set_b = [5.0, 15.0, 8.5]
    data_set_c = [1.0, 2.0, 3.0]
    comparer = DataComparer()
    result1 = comparer.compare_collections(data_set_a, data_set_b)
    print(f"Comparison between A and B: {result1}")
    result2 = comparer.compare_collections(data_set_a, data_set_c)
    print(f"Comparison between A and C: {result2}")
    result3 = comparer.compare_collections(data_set_b, data_set_a)
    print(f"Comparison between B and A: {result3}")
    result4 = comparer.compare_collections(data_set_c, data_set_c)
    print(f"Comparison between C and C: {result4}")