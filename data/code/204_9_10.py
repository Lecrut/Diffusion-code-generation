def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1

def find_median(lst):
    low, high = 0, len(lst) - 1
    while True:
        pivot_index = partition(lst, low, high)
        if pivot_index == (len(lst) - 1) // 2:
            return lst[pivot_index]
        elif pivot_index < (len(lst) - 1) // 2:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

if __name__ == '__main__':
    sample_list_odd = [3, 1, 4, 1, 5, 9, 2]
    median_odd = find_median(sample_list_odd)
    print(f"Median of odd-length list: {median_odd}")
    
    sample_list_even = [3, 1, 4, 1, 5, 9, 2, 6]
    median_even = find_median(sample_list_even)
    print(f"Median of even-length list: {median_even}")