def get_central_element(arr):
    n = len(arr)
    if n == 0:
        return None
    return arr[n // 2]

if __name__ == '__main__':
    print(get_central_element([1, 2, 3, 4, 5]))
    print(get_central_element([1, 2, 3, 4]))
    print(get_central_element([10]))
    print(get_central_element([]))