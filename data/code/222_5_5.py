def min_generator(lst):
    if not lst:
        raise ValueError("List is empty")
    current_min = lst[0]
    for item in lst:
        if item < current_min:
            current_min = item
    yield current_min

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_value = next(min_generator(sample_list))
    print(min_value)