def count_target_value(lst, target):
    return lst.count(target)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 2, 1]
    target_value = 3
    print(count_target_value(sample_list, target_value))