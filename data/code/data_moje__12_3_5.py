def get_middle_element(lst):
    if not lst:
        return None
    n = len(lst)
    middle_index = n // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)