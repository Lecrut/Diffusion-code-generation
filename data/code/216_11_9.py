def find_middle_element(lst):
    length = len(lst)
    return lst[length // 2]

if __name__ == '__main__':
    sample_list = [4, 7, 2, 5, 8]
    print(find_middle_element(sample_list))