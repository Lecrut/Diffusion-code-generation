def count_target(lst, target):
    return lst.count(target)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 2, 3]
    target_value = 2
    print(count_target(sample_list, target_value))