def count_target_value(lst, target):
    return lst.count(target)

if __name__ == '__main__':
    sample_data = [5, 4, 3, 2, 1, 2, 3, 4, 5]
    target_number = 3
    result = count_target_value(sample_data, target_number)
    print(result)