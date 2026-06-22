def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    if n % 2 == 1:
        mid_index = n // 2
        return lst[mid_index]
    else:
        mid_index = n // 2
        return (lst[mid_index - 1] + lst[mid_index]) / 2

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    result = find_middle(sample_list)
    print(result)
    sample_list_even = [1, 3, 5, 7]
    result_even = find_middle(sample_list_even)
    print(result_even)