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
    data_set_a = [10.5, 20.1, 5.0]
    data_set_b = [15.0, 18.3, 7.0]
    data_set_c = [10.5, 20.1, 5.0]
    comparer = DataComparer()
    result1 = comparer.compare_collections(data_set_a, data_set_b)
    print(f"Comparison between A and B: {result1}")
    result2 = comparer.compare_collections(data_set_a, data_set_c)
    print(f"Comparison between A and C: {result2}")
    data_set_d = [1, 2, 3]
    data_set_e = [5, 6, 7]
    result3 = comparer.compare_collections(data_set_d, data_set_e)
    print(f"Comparison between D and E: {result3}")