def get_middle_item(lst):
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_item(sample_list)
    print(result)