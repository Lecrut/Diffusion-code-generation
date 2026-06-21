def find_middle(lst):
    n = len(lst)
    if n == 0:
        raise ValueError("List must not be empty")
    mid_index = n // 2
    if n % 2 == 1:
        return lst[mid_index]
    else:
        lower_index = mid_index - 1
        return (lst[lower_index] + lst[mid_index]) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 2, 3, 4]
    odd_result = find_middle(odd_list)
    even_result = find_middle(even_list)
    print(odd_result)
    print(even_result)