def count_target_value(target_list, target_value):
    return target_list.count(target_value)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 2, 3]
    target = 2
    print(count_target_value(sample_list, target))