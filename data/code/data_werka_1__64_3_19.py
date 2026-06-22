def find_last_index(lst, value):
    return lst[::-1].index(value) if value in lst else -1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6]
    target_value = 3
    print(find_last_index(sample_list, target_value))