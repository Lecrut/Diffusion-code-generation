def min_generator(lst):
    if not lst:
        return None
    min_val = next(iter(lst))
    for item in lst:
        if item < min_val:
            min_val = item
    yield min_val

if __name__ == '__main__':
    sample_list = [7, 8, 3, 4, 2, 9, 1]
    min_value = next(min_generator(sample_list))
    print(min_value)