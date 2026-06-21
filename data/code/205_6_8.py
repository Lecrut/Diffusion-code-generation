class Quicksort:
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def quicksort(arr, low, high):
        if low < high:
            pi = Quicksort.partition(arr, low, high)
            Quicksort.quicksort(arr, low, pi - 1)
            Quicksort.quicksort(arr, pi + 1, high)

    @staticmethod
    def sort(items):
        n = len(items)
        if n <= 1:
            return items
        Quicksort.quicksort(items, 0, n - 1)
        return items

if __name__ == '__main__':
    data = [5, 2, 8, 1, 9]
    sorted_data = Quicksort.sort(data)
    print(sorted_data)