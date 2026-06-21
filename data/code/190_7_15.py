def contains_value(iterable, target):
    return target in iterable

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    search_value = 30
    result = contains_value(sample_list, search_value)
    print(result)