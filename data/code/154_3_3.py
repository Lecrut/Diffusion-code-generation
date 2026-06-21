def count_target_value(lst, target):
    return lst.count(target)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 20, 20, 30]
    target_value = 20
    count = count_target_value(sample_list, target_value)
    print(count)