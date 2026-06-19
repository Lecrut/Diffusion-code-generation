class ArrayComparator:
    def check_adjacent_order(self, arr):
        result = {}
        for i in range(len(arr) - 1):
            result[i] = arr[i] <= arr[i + 1]
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array = [1, 3, 2, 4, 5]
    print(comparator.check_adjacent_order(sample_array))