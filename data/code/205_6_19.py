def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

class Sorter:
    def sort(self, items):
        return quicksort(items)

if __name__ == '__main__':
    sorter = Sorter()
    data1 = [5, 2, 8, 1, 9]
    sorted_data1 = sorter.sort(data1)
    print(sorted_data1)

    data2 = [3, 6, 8, 10, 1, 2, 1]
    sorted_data2 = sorter.sort(data2)
    print(sorted_data2)

    data3 = [7, 5, 3, 1]
    sorted_data3 = sorter.sort(data3)
    print(sorted_data3)