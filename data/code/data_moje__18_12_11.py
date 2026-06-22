def get_median_index(values):
    n = len(values)
    if n == 0:
        return None
    if n == 1:
        return 0
    def partition(start, end):
        pivot = values[end]
        i = start - 1
        for j in range(start, end):
            if values[j] <= pivot:
                i += 1
                values[i], values[j] = values[j], values[i]
        values[i + 1], values[end] = values[end], values[i + 1]
        return i + 1
    def select(start, end, k):
        if start == end:
            return values[start]
        pivot_index = partition(start, end)
        if k == pivot_index:
            return values[k]
        elif k < pivot_index:
            return select(start, pivot_index - 1, k)
        else:
            return select(pivot_index + 1, end, k)
    mid_index = (n - 1) // 2
    return select(0, n - 1, mid_index)

if __name__ == '__main__':
    sample_data = [7, 2, 9, 4, 6, 1, 3]
    result = get_median_index(sample_data)
    print(result)