class ElementComparator:
    @staticmethod
    def compare_adjacent(arr):
        return [arr[i] > arr[i - 1] for i in range(1, len(arr))]

if __name__ == '__main__':
    sample_array = [3.0, 5.5, 2.1, 8.0, 6.0]
    result = ElementComparator.compare_adjacent(sample_array)
    print(result)