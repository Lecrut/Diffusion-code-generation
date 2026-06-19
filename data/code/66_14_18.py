class ArrayComparator:
    @staticmethod
    def compare_adjacent_elements(arr):
        return [arr[i] > arr[i - 1] for i in range(1, len(arr))]

if __name__ == '__main__':
    sample_array = [1.0, 2.5, 3.0, 3.0, 5.1, 6.0, 6.0, 7.5]
    result = ArrayComparator.compare_adjacent_elements(sample_array)
    print(result)