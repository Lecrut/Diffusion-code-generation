def find_smallest(data):
    if not data:
        return None
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest
def smallest_generator(data):
    if not data:
        return
    iterator = iter(data)
    try:
        current_smallest = next(iterator)
    except StopIteration:
        return
    for item in iterator:
        if item < current_smallest:
            current_smallest = item
        yield current_smallest
if __name__ == '__main__':
    sample_list = [5, 1, 8, 3, 9, 2]
    print(list(smallest_generator(sample_list)))