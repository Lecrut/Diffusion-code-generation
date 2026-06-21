def contains_target(iterable, target):
    return target in iterable

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_value = 30
    result = contains_target(sample_list, target_value)
    print(result)