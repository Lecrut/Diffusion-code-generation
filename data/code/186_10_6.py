class Timsorter:
    def __init__(self):
        self.min_run = 32

    def sort(self, arr):
        n = len(arr)
        for i in range(0, n, self.min_run):
            self.insertion_sort(arr, i, min(i + self.min_run - 1, n - 1))
        size = self.min_run
        while size < n:
            for left in range(0, n, size * 2):
                mid = min(n - 1, left + size - 1)
                right = min(left + size * 2 - 1, n - 1)
                self.merge(arr, left, mid, right)
            size *= 2
        return arr

    def insertion_sort(self, arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(self, arr, left, mid, right):
        len1, len2 = mid - left + 1, right - mid
        L, R = arr[left:left+len1], arr[mid+1:mid+1+len2]
        i, j, k = 0, 0, left

        while i < len1 and j < len2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len2:
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    sorter = Timsorter()
    unsorted_integers = [34, 7, 23, 32, 5, 62]
    sorted_integers = sorter.sort(unsorted_integers)
    print(sorted_integers)