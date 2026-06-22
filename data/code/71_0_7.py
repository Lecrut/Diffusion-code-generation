def find_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    if n % 2 == 0:
        mid_index = n // 2
        return lst[mid_index - 1]
    else:
        mid_index = n // 2
        return lst[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = find_middle_element(sample_list)
    print(result)