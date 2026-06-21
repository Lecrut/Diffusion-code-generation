class ArrayComparator:
    def check_adjacent_order(self, arr):
        result = {}
        for index in range(len(arr) - 1):
            current_value = arr[index]
            next_value = arr[index + 1]
            is_non_decreasing = current_value <= next_value
            result[index] = is_non_decreasing
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array = [4, 2, 3, 6, 5, 7, 8]
    print(comparator.check_adjacent_order(sample_array))