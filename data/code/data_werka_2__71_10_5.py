def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    mid_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[mid_index - 1] + lst[mid_index]) / 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = find_middle(sample_list)
    print(result)
    sample_list_even = [1, 2, 3, 4]
    result_even = find_middle(sample_list_even)
    print(result_even)