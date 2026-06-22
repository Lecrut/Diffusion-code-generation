def min_generator(lst):
    if not lst:
        return None
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    yield min_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    min_value = next(min_generator(sample_list))
    print(min_value)