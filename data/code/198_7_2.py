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
        current = next(iterator)
    except StopIteration:
        return
    while True:
        try:
            item = next(iterator)
            if item < current:
                current = item
            yield current
        except StopIteration:
            break
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    gen = smallest_generator(sample_list)
    result = None
    for val in gen:
        if result is None or val < result:
            result = val
    print(result)
    sample_list_2 = [10, 4, 7, 1, 12]
    gen_2 = smallest_generator(sample_list_2)
    result_2 = None
    for val in gen_2:
        if result_2 is None or val < result_2:
            result_2 = val
    print(result_2)
    sample_list_3 = []
    gen_3 = smallest_generator(sample_list_3)
    print(smallest_generator.__name__)