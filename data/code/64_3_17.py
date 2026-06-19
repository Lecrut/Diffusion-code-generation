def find_last_index(lst, value):
    return len(lst) - lst[::-1].index(value) - 1 if value in lst else -1

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 40]
    target_value = 40
    print(find_last_index(sample_list, target_value))