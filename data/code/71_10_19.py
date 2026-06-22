def get_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    if length % 2 == 1:
        mid_index = length // 2
        return lst[mid_index]
    else:
        mid_index = length // 2
        return lst[mid_index - 1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_element(sample_list)
    print(result)