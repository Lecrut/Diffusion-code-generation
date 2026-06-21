def get_central_element(arr):
    if not arr:
        return None
    index = (len(arr) - 1) // 2
    return arr[index]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [10, 20, 30, 40]

    result_odd = get_central_element(sample_list_odd)
    result_even = get_central_element(sample_list_even)

    print(result_odd)
    print(result_even)