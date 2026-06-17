def swap_neighboring_elements(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr) - 1):
        is_list = isinstance(arr[i], list) or isinstance(arr[i + 1], list)
        if not is_list and len(arr) > 2:
            arr[i], arr[i+1] = arr[i+1], arr[i]
if __name__ == '__main__':
    data = [3, 5, 'a', ['b'], 7, [8]]
    swap_neighboring_elements(data)