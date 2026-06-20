def find_middle_element(lst):
    return lst[(len(lst) - 1) // 2]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1]
    print(find_middle_element(sample_list))