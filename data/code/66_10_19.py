class ArrayComparator:
    def check_adjacent_order(self, arr):
        return {i: arr[i] <= arr[i + 1] for i in range(len(arr) - 1)}

if __name__ == '__main__':
    comparator = ArrayComparator()
    result = comparator.check_adjacent_order([1, 2, 3, 2, 5])
    print(result)