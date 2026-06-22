class ArrayComparator:
    NON_DECREASING = "non_decreasing"

    @staticmethod
    def is_non_decreasing(a, b):
        return a <= b

    def check_adjacent_order(self, arr):
        result = {}
        for i in range(len(arr) - 1):
            result[i] = self.is_non_decreasing(arr[i], arr[i + 1])
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array_1 = [3, 5, 2, 6, 8, 7]
    sample_array_2 = [1, 2, 3, 4, 5]
    sample_array_3 = [10, 10, 10, 10]
    sample_array_4 = [9, 8, 7, 6, 5]
    sample_array_5 = [1]
    sample_array_6 = []

    print(f"Sample Array 1: {comparator.check_adjacent_order(sample_array_1)}")
    print(f"Sample Array 2: {comparator.check_adjacent_order(sample_array_2)}")
    print(f"Sample Array 3: {comparator.check_adjacent_order(sample_array_3)}")
    print(f"Sample Array 4: {comparator.check_adjacent_order(sample_array_4)}")
    print(f"Sample Array 5: {comparator.check_adjacent_order(sample_array_5)}")
    print(f"Sample Array 6: {comparator.check_adjacent_order(sample_array_6)}")