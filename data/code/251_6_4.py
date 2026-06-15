def find_largest(data_iter):
    try:
        first_item = next(data_iter)
    except StopIteration:
        return None
    largest = first_item
    for number in data_iter:
        if number > largest:
            largest = number
    return largest
def largest_generator(iterable):
    if not iterable:
        return
    iterator = iter(iterable)
    try:
        current_max = next(iterator)
    except StopIteration:
        return
    for number in iterator:
        if number > current_max:
            current_max = number
        yield current_max
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    print(list(largest_generator(sample_data)))