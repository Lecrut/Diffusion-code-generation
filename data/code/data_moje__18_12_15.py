def get_median_index(lst):
    if not lst:
        return None
    n = len(lst)
    indices = list(range(n))
    def swap(i, j):
        indices[i], indices[j] = indices[j], indices[i]
    def partition(low, high):
        pivot = indices[high]
        pi_val = lst[pivot]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pi_val:
                i += 1
                swap(i, j)
        swap(i + 1, high)
        return i + 1
    def quickselect(low, high, k):
        if low == high:
            return indices[low]
        pivot_index = partition(low, high)
        if k == pivot_index:
            return indices[k]
        elif k < pivot_index:
            return quickselect(low, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, high, k)
    if n % 2 == 1:
        middle = n // 2
        idx = quickselect(0, n - 1, middle)
        return idx
    else:
        idx1 = quickselect(0, n - 1, n // 2 - 1)
        idx2 = quickselect(0, n - 1, n // 2)
        if lst[idx1] > lst[idx2]:
            return idx2
        elif lst[idx1] < lst[idx2]:
            return idx1
        else:
            return idx1

if __name__ == '__main__':
    data = [10, 4, 20, 15, 30]
    result = get_median_index(data)
    print(result)