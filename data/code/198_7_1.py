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
    current_smallest = data[0]
    yield current_smallest
    for item in data[1:]:
        if item < current_smallest:
            current_smallest = item
            yield current_smallest
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    generator = smallest_generator(sample_list)
    result = None
    for value in generator:
        result = value
    print(result)
    sample_list_empty = []
    generator_empty = smallest_generator(sample_list_empty)
    result_empty = None
    for value in generator_empty:
        result_empty = value
    print(result_empty)
    sample_list_single = [42]
    generator_single = smallest_generator(sample_list_single)
    result_single = None
    for value in generator_single:
        result_single = value
    print(result_single)