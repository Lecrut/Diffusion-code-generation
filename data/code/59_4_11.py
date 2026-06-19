def find_middle_element(lst):
    if not lst:
        return None
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(find_middle_element(sample_list))