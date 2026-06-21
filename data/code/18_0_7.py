def find_middle(arr):
    n = len(arr)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 == 0:
        if mid_index - 1 >= 0:
            left = arr[mid_index - 1]
            right = arr[mid_index]
            return (left + right) / 2.0
        return right
    else:
        return arr[mid_index]

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8, 10, 12]
    print(find_middle(odd_list))
    print(find_middle(even_list))