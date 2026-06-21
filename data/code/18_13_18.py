def get_central_element(arr):
    if not arr:
        return None
    mid_index = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[mid_index - 1] + arr[mid_index]) / 2
    else:
        return arr[mid_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4, 5, 6]
    print(get_central_element(odd_list))
    print(get_central_element(even_list))