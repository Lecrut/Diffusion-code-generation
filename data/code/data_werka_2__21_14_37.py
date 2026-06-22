class QuickSorter:
    def __init__(self, arr):
        if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
            raise ValueError("Input must be a list of integers")
        self.arr = arr

    def sort(self):
        self._quicksort(0, len(self.arr) - 1)
        return self.arr

    def _quicksort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quicksort(low, pi - 1)
            self._quicksort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

if __name__ == '__main__':
    sample_values = [9, 3, 7, 6, 2, 8, 5, 1, 4]
    sorter = QuickSorter(sample_values)
    sorted_values = sorter.sort()
    print(sorted_values)