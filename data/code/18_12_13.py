def get_median_index(values):
    if not values:
        raise ValueError("List cannot be empty")
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        mid = n // 2
        return (values[mid - 1] + values[mid]) / 2

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, low, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, high, k)

def calculate_median_value(values):
    if not values:
        raise ValueError("List cannot be empty")
    n = len(values)
    if n % 2 == 1:
        return quick_select(values.copy(), 0, n - 1, n // 2)
    else:
        temp = values.copy()
        mid = n // 2
        val1 = quick_select(temp, 0, n - 1, mid - 1)
        for i, x in enumerate(values):
            if i == 0 or x > val1:
                temp[i] = x
            else:
                temp[i] = float('inf')
        temp[n // 2] = float('inf')
        val2 = quick_select(temp, 0, n - 1, mid)
        return (val1 + val2) / 2

if __name__ == '__main__':
    sample_data = [7, 1, 9, 3, 5, 2, 8]
    median_value = calculate_median_value(sample_data)
    print(median_value)