class Quicksort:
    PIVOT_THRESHOLD = 10

    @staticmethod
    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    @staticmethod
    def quicksort(items, low, high):
        if low < high:
            pi = Quicksort.partition(items, low, high)
            Quicksort.quicksort(items, low, pi - 1)
            Quicksort.quicksort(items, pi + 1, high)

    @staticmethod
    def sort(items):
        if len(items) <= Quicksort.PIVOT_THRESHOLD:
            return sorted(items)
        else:
            Quicksort.quicksort(items, 0, len(items) - 1)
            return items

if __name__ == '__main__':
    data = [5, 2, 8, 1, 9]
    sorted_data = Quicksort.sort(data)
    print(sorted_data)