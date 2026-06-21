def find_middle(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [10, 20, 30, 40]
    sample_list_3 = [7]
    sample_list_4 = []
    print(find_middle(sample_list_1))
    print(find_middle(sample_list_2))
    print(find_middle(sample_list_3))
    try:
        print(find_middle(sample_list_4))
    except IndexError:
        print(None)