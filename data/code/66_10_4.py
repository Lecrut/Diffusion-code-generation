class ArrayComparator:
    def check_adjacent_order(self, arr):
        result = {}
        for i in range(len(arr) - 1):
            result[i] = arr[i] <= arr[i + 1]
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array = [3, 5, 2, 6, 8, 7]
    print(comparator.check_adjacent_order(sample_array))