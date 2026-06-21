def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

def quickselect_median(data, k):
    if len(data) == 0:
        return None
    low, high = 0, len(data) - 1
    while True:
        pivot_index = partition(data, low, high)
        if pivot_index == k:
            return data[k]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(quickselect_median(list1, len(list1) // 2))
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(quickselect_median(list2, len(list2) // 2))