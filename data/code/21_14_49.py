class QuickSorter:
    def __init__(self, arr):
        if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
            raise ValueError("Input must be a list of integers")
        self.arr = arr

    @staticmethod
    def _partition(low, high, arr):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(self, low, high):
        if low < high:
            pi = QuickSorter._partition(low, high, self.arr)
            self._quicksort(low, pi - 1)
            self._quicksort(pi + 1, high)

    def sort(self):
        self._quicksort(0, len(self.arr) - 1)
        return self.arr

if __name__ == '__main__':
    sample_values = [5, 3, 8, 4, 2, 7, 1, 10]
    sorter = QuickSorter(sample_values)
    sorted_values = sorter.sort()
    print(sorted_values)