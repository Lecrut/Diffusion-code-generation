def count_target(target, lst):
    return lst.count(target)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 2, 3]
    target_value = 2
    print(count_target(target_value, sample_list))