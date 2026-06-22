class QuickSorter:
    def __init__(self, arr):
        if not isinstance(arr, list):
            raise ValueError("Input must be a list.")
        self.arr = arr

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def quicksort_recursive(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quicksort_recursive(low, pi - 1)
            self.quicksort_recursive(pi + 1, high)

    def sort(self):
        self.quicksort_recursive(0, len(self.arr) - 1)
        return self.arr

if __name__ == '__main__':
    sample_values = [5, 2, 9, 1, 5, 6]
    sorter = QuickSorter(sample_values)
    sorted_values = sorter.sort()
    print(sorted_values)