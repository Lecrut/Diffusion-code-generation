def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2
    if length % 2 == 0:
        return (lst[middle_index - 1] + lst[middle_index]) / 2
    else:
        return lst[middle_index]

if __name__ == '__main__':
    sample_list = [4, 7, 2, 5, 8]
    print(find_middle_element(sample_list))