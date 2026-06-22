def find_middle_element(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    n = len(lst)
    middle_index = (n - 1) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [3.5, 4.6, 5.7, 6.8, 7.9]
    print(find_middle_element(sample_list))