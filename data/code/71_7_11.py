def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    mid_index = length // 2
    if length % 2 == 0:
        val1 = lst[mid_index - 1]
        val2 = lst[mid_index]
        return (val1 + val2) / 2
    else:
        return lst[mid_index]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    result = find_middle(sample_list)
    print(result)
    
    sample_list_even = [1, 3, 5, 7]
    result_even = find_middle(sample_list_even)
    print(result_even)