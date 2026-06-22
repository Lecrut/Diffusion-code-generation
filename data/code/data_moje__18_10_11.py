def get_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)