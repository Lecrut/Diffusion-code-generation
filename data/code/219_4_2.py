def find_max_generator(iterable):
    try:
        iterator = iter(iterable)
        first_item = next(iterator)
    except StopIteration:
        return
    current_max = first_item
    yield current_max
    for item in iterator:
        if item > current_max:
            current_max = item
        yield current_max
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    print("Maximum value found:")
    for max_val in find_max_generator(sample_list):
        print(max_val)