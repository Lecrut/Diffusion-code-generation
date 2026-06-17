def find_max_iterable(iterable):
    iterator = iter(iterable)
    try:
        current_max = next(iterator)
    except StopIteration:
        raise ValueError("The iterable is empty")
    for item in iterator:
        if item > current_max:
            current_max = item
    return current_max
if __name__ == '__main__':
    sample_data = [3, 7, -2, 90, 15]
    result = find_max_iterable(sample_data)
    print(result)