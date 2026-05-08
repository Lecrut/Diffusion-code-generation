def smallest_so_far(data):
    if not data:
        return
    smallest = data[0]
    yield smallest
    for item in data[1:]:
        if item < smallest:
            smallest = item
        yield smallest
if __name__ == '__main__':
    input_list = [5, 2, 8, 1, 9, 3]
    generator = smallest_so_far(input_list)
    result = list(generator)
    print(result)